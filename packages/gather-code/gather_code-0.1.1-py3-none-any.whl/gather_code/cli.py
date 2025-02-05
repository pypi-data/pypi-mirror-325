#!/usr/bin/env python3
"""
gather_code - Gather your codebase into a single file with a directory tree and file contents.

Usage examples:
  # Gather everything (tracked) into all_code.txt:
  gather-code --root . --output all_code.txt

  # Only include .py and .js files:
  gather-code --root . --output full_code.txt --whitelist py,js

  # Exclude images (png, jpg):
  gather-code --root . --output full_code.txt --blacklist png,jpg
"""

import argparse
import os
import subprocess
import sys

# --------------------------
# Helper Functions
# --------------------------

def get_tracked_files(root_dir):
    """
    Run 'git ls-files' from the given root directory.
    Returns a set of file paths (using forward slashes) that are tracked.
    """
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
    """
    Convert a comma-separated list of extensions (e.g. "py,js,html")
    into a set of extensions (with a leading dot and lowercased).
    """
    ext_set = set()
    for ext in ext_string.split(","):
        ext = ext.strip()
        if ext and not ext.startswith("."):
            ext = "." + ext
        if ext:
            ext_set.add(ext.lower())
    return ext_set

def generate_directory_tree(root, included_files):
    """
    Generate a directory tree (as a string) that shows only files whose
    relative paths (from root, using forward slashes) appear in the included_files set.
    
    Directories that contain no included files are omitted.
    The special '.git' directory is always skipped.
    """
    lines = []
    root_name = os.path.basename(os.path.abspath(root))
    lines.append(f"{root_name}/")

    def rec(current_path, current_rel, prefix=""):
        try:
            entries = sorted(os.listdir(current_path))
        except PermissionError:
            return
        
        # Filter entries: include only directories that have at least one included file
        # or files that are in the included_files set.
        filtered_entries = []
        for entry in entries:
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                if entry == ".git":
                    continue  # Skip .git entirely.
                # Compute relative path for the directory.
                dir_rel = entry if not current_rel else current_rel + "/" + entry
                # Include this directory if any included file starts with this directory's path.
                if any(f == dir_rel or f.startswith(dir_rel + "/") for f in included_files):
                    filtered_entries.append(entry)
            else:
                # For files, compute the relative path.
                file_rel = entry if not current_rel else current_rel + "/" + entry
                if file_rel in included_files:
                    filtered_entries.append(entry)
        count = len(filtered_entries)
        for idx, entry in enumerate(filtered_entries):
            is_last = (idx == count - 1)
            branch = "└── " if is_last else "├── "
            new_prefix = prefix + ("    " if is_last else "│   ")
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                lines.append(prefix + branch + entry + "/")
                new_rel = entry if not current_rel else current_rel + "/" + entry
                rec(full_path, new_rel, new_prefix)
            else:
                lines.append(prefix + branch + entry)
    
    rec(root, "")
    return "\n".join(lines)

# --------------------------
# Main Function
# --------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Gather your codebase into a single file with a directory tree and file content blocks."
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

    # Resolve absolute paths.
    root_dir = os.path.abspath(args.root)
    output_file_path = os.path.abspath(args.output)
    # Compute output file's relative path (using forward slashes) with respect to the root.
    output_file_rel = os.path.relpath(output_file_path, root_dir).replace(os.sep, "/")

    # Get tracked files.
    tracked_files = get_tracked_files(root_dir)

    # Build final list of files to include in the gathered output.
    # (Exclude the output file itself.)
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

    # Create a set of included file paths for use in the directory tree.
    included_files = set(final_files)

    # Build the directory tree using only the included files.
    tree_str = "Directory Tree:\n" + generate_directory_tree(root_dir, included_files)

    # Prepare the header separator.
    header_sep = "# " + "=" * 21

    # Open the output file and write the directory tree and file content blocks.
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
