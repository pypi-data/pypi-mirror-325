# Gather Code

**Gather Code** is a command-line tool that aggregates your entire codebase into a single file. It scans your project (respecting your `.gitignore` rules), generates a directory tree view, and appends the contents of each file—each with a clear header—into one comprehensive output file. This is ideal for creating snapshots of your code, sharing your project in a consolidated form, or archiving your work.

## Features

- **Respects `.gitignore`:** Only processes Git-tracked files.
- **Directory Tree Visualization:** Generates a neat directory tree at the top of the output file, marking excluded files or directories.
- **Content Aggregation:** Inserts each file’s content below a header that includes its relative path.
- **Extension Filtering:** Use whitelist or blacklist options to include or exclude files by their extensions.
- **Easy-to-Use CLI:** Quickly gather your codebase with simple command-line options.

## Installation

### From PyPI

If published on PyPI, you can install it with:

```bash
pip install gather_code
```

### From Source

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/gather_code.git
cd gather_code
pip install -e .
```

This will install the command-line tool `gather-code`.

## Usage

After installation, you can run the tool directly from the command line:

```bash
gather-code --root . --output full_code.txt
```

### Options

- `--root`: The root directory of your repository (default is the current directory).
- `--output`: The file where the aggregated code will be saved (default is `all_code.txt`).
- `--whitelist`: A comma-separated list of file extensions to include (e.g., `py,js,html`).
- `--blacklist`: A comma-separated list of file extensions to exclude (e.g., `png,jpg,exe`).

### Examples

- **Aggregate Entire Codebase:**

  ```bash
  gather-code --root . --output full_code.txt
  ```

- **Include Only Python and JavaScript Files:**

  ```bash
  gather-code --root . --output code.txt --whitelist py,js
  ```

- **Exclude Image Files:**

  ```bash
  gather-code --root . --output code.txt --blacklist png,jpg
  ```

## Contributing

Contributions are welcome! If you have ideas for improvements or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push your branch.
4. Open a pull request detailing your changes.

For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Developed by [Oleksii Furman](https://github.com/ofurman).

## Acknowledgements

Thanks to the open-source community and all contributors who help improve this tool!
