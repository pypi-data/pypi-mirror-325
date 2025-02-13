# Roysh - A Python-based Shell

Roysh is a simple yet powerful Python-based shell that provides familiar shell functionality with tab completion support.

## Features

- Interactive command-line interface
- Tab completion for commands and file paths
- Built-in shell commands
- Command output redirection
- Path-based command execution
- Cross-platform support

## Installation

Install using pip:

```bash
pip install roysh
```

## Usage

Start the shell by running:

```bash
roysh
```

### Built-in Commands

| Command | Description |
|---------|-------------|
| `echo [text]` | Print text to stdout |
| `exit [code]` | Exit the shell (optional status code) |
| `type <command>` | Show command type/location |
| `pwd` | Print working directory |
| `cd [path]` | Change directory (defaults to HOME) |

### Output Redirection

Roysh supports standard output redirection operators:

| Operator | Description |
|----------|-------------|
| `>` | Redirect stdout to file (overwrite) |
| `>>` | Append stdout to file |
| `2>` | Redirect stderr to file (overwrite) |
| `2>>` | Append stderr to file |

### Examples

```bash
# Basic command usage
$ echo Hello World
Hello World

# Working with directories
$ pwd
/home/user
$ cd /tmp
$ pwd
/tmp

# Output redirection
$ echo "log entry" >> log.txt
$ echo "error message" 2> errors.txt

# Command information
$ type echo
echo is a shell builtin
$ type python
python is /usr/bin/python
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Developed by Nishan Roy
```