<h1 align="center">
<img src="./media/bonzai_dark_long.png" width="800">
</h1><br>

# Bonzai: A Minimalist Directory Tree CLI Tool & Python Library

## Overview
Bonzai is a command-line interface (CLI) tool and Python library designed for working with directory structures in a clear, compact, and visual way. It allows users to generate directory trees, save them as JSON files, load them from JSON, and compute relative paths between directories. The name "Bonsai" reflects the tool's ability to take something complex, like a filesystem, and represent it in an organized and elegant manner.

## Features
- **Visualize Directory Trees**: Generate and display the structure of directories with optional details like file permissions and file sizes.

- **Export to JSON**: Save the directory tree structure as a JSON file for later use or sharing.

- **Load from JSON**: Load a directory tree from a JSON file and visualize it.

- **Python API**: Compute the relative path between two directories.

- **Relative Paths**: Import Bonzai as a Python library for programmatic directory tree manipulation.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/abhi-pixel1/bonsai.git
```
2. Install the tool using pip:
```bash
pip install .
```


## CLI Usage
The Bonzai CLI includes the following commands:
1. ### `tree`
Generates and displays the directory tree for a given directory.

#### Syntax:
```bash
bonsai tree [DIRECTORY_PATH] [OPTIONS]
```
#### Arguments:

- `DIRECTORY_PATH`: The directory for which the tree should be generated (required).

#### Options:

- `-p`, `--show-permissions`: Include file permissions in the tree output.

- `-s`, `--show-size`: Include file sizes in the tree output.

#### Example:
```bash
bonzai tree ./my_directory -p -s
```

2. ### `save-tree`
Saves the directory tree structure of a given directory to a JSON file.

#### Syntax:
```bash
bonzai save-tree [DIRECTORY_PATH] [OUTPUT_FILE]
```

#### Arguments:

- `DIRECTORY_PATH`: The directory for which the tree should be saved (required).
- `OUTPUT_FILE`: The file where the JSON output should be saved. Must have a .json extension.

#### Example:

```bash
bonzai save-tree ./my_directory tree.json
```

3. ### `jtree`
Loads a directory tree structure from a JSON file and displays it.

#### Syntax:
```bash
bonzai jtree [JSON_FILE] [OPTIONS]
```

#### Arguments:

- `JSON_FILE`: Path to the JSON file containing the directory tree structure (required).

#### Options:

- `-p`, `--show-permissions`: Include file permissions in the tree output.
- `-s`,`--show-size`:  Include file sizes in the tree output.

#### Example:

```bash
bonzai jtree tree.json -p -s
```

4. ### `relative`
Calculates and displays the relative path between two directories.

#### Syntax:
```bash
bonzai relative [DESTINATION_PATH] [BASE_PATH]
```

#### Arguments:

- `DESTINATION_PATH`: The target directory.
- `BASE_PATH`: The starting directory.

#### Example:

```bash
bonzai relative ./my_directory ./another_directory
```

## Python API Usage
Bonsai can also be used as a Python library to generate and visualize directory trees programmatically.

### Importing Bonzai
```python
from bonzai import generate_directory_tree, visualize_tree
```

### Generating a Directory Tree
```python
from bonzai import generate_directory_tree

tree = generate_directory_tree("./my_directory")
print(tree)
```

### Visualizing a Directory Tree
```python
from bonzai import visualize_tree

print(visualize_tree(tree, show_permissions=True, show_size=True))
```

## Contributers:
[![Contributors](https://contrib.rocks/image?repo=abhi-pixel1/bonsai)](https://github.com/abhi-pixel1/bonsai/graphs/contributors)


## License

This project is licensed under the MIT License. See the LICENSE file for details.

