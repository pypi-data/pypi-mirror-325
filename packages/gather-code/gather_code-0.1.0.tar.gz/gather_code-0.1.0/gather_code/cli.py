# gather_code/cli.py
import argparse
import os
import subprocess
import sys

def get_tracked_files(root_dir):
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=root_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        files = set(result.stdout.splitlines())
        return files
    except subprocess.CalledProcessError as e:
        print("Error running 'git ls-files':", e.stderr, file=sys.stderr)
        sys.exit(1)

def parse_extensions(ext_string):
    ext_set = set()
    for ext in ext_string.split(","):
        ext = ext.strip()
        if ext and not ext.startswith("."):
            ext = "." + ext
        if ext:
            ext_set.add(ext.lower())
    return ext_set

def generate_directory_tree(root, tracked_files, output_file_rel):
    lines = []
    root_name = os.path.basename(os.path.abspath(root))
    lines.append(f"{root_name}/")
    
    def rec(dir_path, prefix=""):
        try:
            entries = sorted(os.listdir(dir_path))
        except PermissionError:
            return
            
        count = len(entries)
        for idx, entry in enumerate(entries):
            full_path = os.path.join(dir_path, entry)
            rel_path = os.path.relpath(full_path, root).replace(os.sep, "/")
            is_last = (idx == count - 1)
            branch = "└── " if is_last else "├── "
            new_prefix = prefix + ("    " if is_last else "│   ")
            if os.path.isdir(full_path):
                mark = " [EXCLUDED]" if entry == ".git" else ""
                lines.append(prefix + branch + entry + "/" + mark)
                if entry != ".git":
                    rec(full_path, new_prefix)
            else:
                mark = ""
                if (rel_path not in tracked_files) and (rel_path != output_file_rel):
                    mark = " [EXCLUDED]"
                lines.append(prefix + branch + entry + mark)
    
    rec(root)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Gather your codebase into a single file (with directory tree and file content blocks)."
    )
    parser.add_argument("--root", type=str, default=".",
                        help="Root directory of the repository (default: current directory)")
    parser.add_argument("--output", type=str, default="all_code.txt",
                        help="Output file to write the gathered code (default: all_code.txt)")
    parser.add_argument("--whitelist", type=str,
                        help="Comma-separated list of file extensions to include (e.g., 'py,js,html').")
    parser.add_argument("--blacklist", type=str,
                        help="Comma-separated list of file extensions to exclude (e.g., 'png,jpg,exe').")
    args = parser.parse_args()

    root_dir = os.path.abspath(args.root)
    output_file_path = os.path.abspath(args.output)
    output_file_rel = os.path.relpath(output_file_path, root_dir).replace(os.sep, "/")
    tracked_files = get_tracked_files(root_dir)

    final_files = []
    for f in tracked_files:
        if f == output_file_rel:
            continue
        _, ext = os.path.splitext(f)
        ext = ext.lower()
        if args.whitelist:
            whitelist = parse_extensions(args.whitelist)
            if ext not in whitelist:
                continue
        if args.blacklist:
            blacklist = parse_extensions(args.blacklist)
            if ext in blacklist:
                continue
        final_files.append(f)
    final_files = sorted(final_files)
    
    tree_str = "Directory Tree:\n" + generate_directory_tree(root_dir, tracked_files, output_file_rel)
    header_sep = "# " + "=" * 21

    try:
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(tree_str + "\n\n")
            for f in final_files:
                display_path = f.replace("/", os.sep)
                outfile.write(header_sep + "\n")
                outfile.write(f"# File: {display_path}\n")
                outfile.write(header_sep + "\n\n")
                abs_file_path = os.path.join(root_dir, f)
                try:
                    with open(abs_file_path, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"Error reading file '{abs_file_path}': {e}", file=sys.stderr)
                    outfile.write(f"\n# [Error reading file: {e}]\n")
                outfile.write("\n\n")
    except Exception as e:
        print("Error writing to output file:", e, file=sys.stderr)
        sys.exit(1)
    
    print(f"All code gathered into '{output_file_path}'")

if __name__ == "__main__":
    main()
