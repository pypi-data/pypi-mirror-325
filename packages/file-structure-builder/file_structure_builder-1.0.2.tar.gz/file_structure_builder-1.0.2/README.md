# File Structure Builder

A Python-based tool that allows users to generate and manage file structures from a structured definition file. It can be used via a command-line interface (CLI) to automate project scaffolding.

## Features
- Build directory structures from a text definition.
- Parse structured files to generate folder hierarchies.
- CLI interface for ease of use.
- Supports interactive mode (future implementation).

## Project Structure
```
file-structure-builder/
├── file_structure_builder/
│   ├── __init__.py
│   ├── builder.py          # Core logic for building file structures
│   ├── parser.py           # Logic for parsing input (file or API)
│   └── utils.py            # Utility functions
├── tests/                  # Unit tests
│   └── test_builder.py
├── cli.py                  # CLI entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aliasgharmirhshai/File-Structure-Builder.git
   cd file-structure-builder
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### CLI Usage
Run the CLI with:
```sh
python cli.py --file structure.txt
```

#### Options:
- `--file`, `-f <path>`: Path to the structure definition file.
- `--api`, `-a` (Not yet implemented): Fetch structure from an API.
- `--interactive`, `-i` (Not yet implemented): Interactive mode to build structures.

### Example Structure File
Create a file named `structure.txt` with the following content:
```
project/
    ├── src/
    │   ├── main.py
    │   ├── utils.py
    ├── README.md
    ├── .gitignore
```
Run the command:
```sh
python cli.py --file structure.txt
```
This will generate the corresponding file structure in your current directory.

## Module Overview
### `file_structure_builder/builder.py`
Handles creating directories and files based on a structured input list.

### `file_structure_builder/parser.py`
Parses text-based structure files and converts them into a structured format for processing.

### `file_structure_builder/utils.py`
Placeholder for utility functions (future expansion).

## Roadmap
- [ ] Implement API-based structure fetching.
- [ ] Add interactive mode.
- [ ] Improve error handling and logging.

## Contributions
Contributions are welcome! Feel free to submit issues and pull requests.

## Author
[Aliasghar Mirshahi](https://github.com/aliasgharmirhshai/)

