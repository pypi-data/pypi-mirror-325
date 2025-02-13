import sys
import os
import subprocess
import shlex

# Handle readline import for different platforms
try:
    import readline
except ImportError:
    import pyreadline3 as readline

def extract_after_third_slash(command):
    """Extracts the portion of the command after the third slash (/)"""
    parts = command.split("/")
    if len(parts) > 3:
        return "/".join(parts[3:])
    return command

def get_executables_from_path():
    """Get list of executable files from PATH directories"""
    executables = []
    extensions = ['.exe', '.bat', '.cmd', ''] if os.name == 'nt' else ['']
    path_sep = ';' if os.name == 'nt' else ':'
    
    for directory in os.environ.get("PATH", "").split(path_sep):
        try:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                # Check if the file has an executable extension on Windows
                if os.name == 'nt':
                    file_name, file_ext = os.path.splitext(file.lower())
                    if file_ext not in extensions:
                        continue
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    # Remove extension for consistency
                    base_name = os.path.splitext(file)[0]
                    executables.append(base_name)
        except OSError:
            continue
    return executables

def get_common_prefix(matches):
    """Find the longest common prefix of all matches"""
    if not matches:
        return ""
    if len(matches) == 1:
        return matches[0]
    
    reference = matches[0]
    
    for i in range(len(reference)):
        for other in matches[1:]:
            if i >= len(other) or other[i] != reference[i]:
                return reference[:i]
    
    return reference

def get_matches(text):
    """Get all matching commands for the given text"""
    builtins = ["echo", "exit", "type", "pwd", "cd", "list"]
    all_commands = builtins + get_executables_from_path()
    return sorted(set(cmd for cmd in all_commands if cmd.startswith(text)))

def complete(text, state):
    """Autocomplete callback for readline"""
    matches = get_matches(text)
    
    if not matches:
        return None
        
    if state == 0:
        if len(matches) == 1:
            return matches[0] + " "
        else:
            common = get_common_prefix(matches)
            if common != text:
                return common
            sys.stdout.write('\a')
            sys.stdout.flush()
            print()
            print("  ".join(matches))
            sys.stdout.write("$ " + text)
            sys.stdout.flush()
            return text
    
    return None

def get_installed_packages():
    """Get list of installed Python packages"""
    try:
        import pkg_resources
        return sorted([f"{dist.key} {dist.version}" for dist in pkg_resources.working_set])
    except Exception:
        return ["Error: Unable to fetch installed packages"]

def get_roysh_commands():
    """Get list of roysh commands with descriptions"""
    commands = {
        "echo": "Print text to stdout",
        "exit": "Exit the shell (optional: exit <code>)",
        "type": "Show command type/location",
        "pwd": "Print working directory",
        "cd": "Change directory (defaults to HOME)",
        "list": "List available commands or installed packages",
    }
    return commands

def main():
    # Display welcome message
    print("\nRoysh - Shell by Python")
    print("Developed by Nishan Roy")
    print("Type 'exit' to quit\n")

    # Set up readline with our completer
    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)
    
    # Define the list of built-in commands
    builtins = {"echo", "exit", "type", "pwd", "cd", "list"}
    
    while True:
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            # Read user input (readline will handle tab completion)
            command = input().strip()
            
            # Check for output redirection
            output_file = None
            error_file = None
            append_mode = False
            append_error_mode = False
            
            if " 2>> " in command:
                parts = command.split(" 2>> ", 1)
                command = parts[0].strip()
                error_file = parts[1].strip()
                append_error_mode = True
            elif " 2> " in command:
                parts = command.split(" 2> ", 1)
                command = parts[0].strip()
                error_file = parts[1].strip()
            elif " >> " in command or " 1>> " in command:
                parts = command.split(" >> ", 1) if " >> " in command else command.split(" 1>> ", 1)
                command = parts[0].strip()
                output_file = parts[1].strip()
                append_mode = True
            elif " > " in command or " 1> " in command:
                parts = command.split(" > ", 1) if " > " in command else command.split(" 1> ", 1)
                command = parts[0].strip()
                output_file = parts[1].strip()
            
            # Parse input to handle quotes
            args = shlex.split(command, posix=True)
            if not args:
                continue
                
            # Save original stdout/stderr if we need to redirect
            original_stdout = None
            original_stderr = None
            
            try:
                if output_file:
                    original_stdout = sys.stdout
                    sys.stdout = open(output_file, 'a' if append_mode else 'w')
                if error_file:
                    original_stderr = sys.stderr
                    sys.stderr = open(error_file, 'a' if append_error_mode else 'w')
                
                cmd = args[0]
                # Handle built-in commands
                if cmd == "exit":
                    if len(args) > 1 and args[1].isdigit():
                        exit_code = int(args[1])
                    else:
                        exit_code = 0
                    sys.exit(exit_code)
                elif cmd == "list":
                    if len(args) > 1 and args[1] == "packages":
                        packages = get_installed_packages()
                        for package in packages:
                            print(package)
                    else:
                        print("\nAvailable Roysh Commands:")
                        print("----------------------")
                        commands = get_roysh_commands()
                        for cmd_name, description in commands.items():
                            print(f"{cmd_name:<10} - {description}")
                        print("\nUsage:")
                        print("list         - Show this help")
                        print("list packages - Show installed Python packages\n")
                elif cmd == "type":
                    if len(args) < 2:
                        print("type: missing operand")
                        continue
                    cmd_to_check = args[1]
                    if cmd_to_check in builtins:
                        print(f"{cmd_to_check} is a shell builtin")
                    else:
                        found = False
                        for directory in os.environ["PATH"].split(":"):
                            command_path = os.path.join(directory, cmd_to_check)
                            if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
                                print(f"{cmd_to_check} is {command_path}")
                                found = True
                                break
                        if not found:
                            print(f"{cmd_to_check}: not found")
                elif cmd == "pwd":
                    print(os.getcwd())
                elif cmd == "cd":
                    if len(args) < 2:
                        target_dir = os.environ.get("HOME", "/")
                    else:
                        target_dir = args[1]
                    if target_dir == "~":
                        target_dir = os.environ.get("HOME", "/")
                    try:
                        os.chdir(target_dir)
                    except FileNotFoundError:
                        print(f"cd: {target_dir}: No such file or directory")
                    except PermissionError:
                        print(f"cd: {target_dir}: Permission denied")
                elif cmd == "echo":
                    print(" ".join(args[1:]))
                else:
                    found = False
                    extensions = ['.exe', '.bat', '.cmd', ''] if os.name == 'nt' else ['']
                    for directory in os.environ["PATH"].split(os.pathsep):
                        for ext in extensions:
                            program_path = os.path.join(directory, cmd + ext)
                            if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
                                found = True
                                try:
                                    result = subprocess.run(
                                        [program_path] + args[1:],
                                        capture_output=True,
                                        text=True,
                                    )
                                    if result.stdout:
                                        print(result.stdout.strip())
                                    if result.stderr:
                                        print(result.stderr.strip(), file=sys.stderr)
                                except Exception as e:
                                    print(f"Error running {cmd}: {e}", file=sys.stderr)
                                break
                        if found:
                            break
                    if not found:
                        print(f"{cmd}: not found")
            finally:
                if output_file and original_stdout:
                    sys.stdout.close()
                    sys.stdout = original_stdout
                if error_file and original_stderr:
                    sys.stderr.close()
                    sys.stderr = original_stderr
        except EOFError:
            sys.exit(0)

if __name__ == "__main__":
    main() 