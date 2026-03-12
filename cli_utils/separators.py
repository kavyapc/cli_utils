# cli_utils/separators.py

def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_custom_separator(char, length):
    print(char * int(length))

def print_box(message):
    """Prints a message inside a yellow ASCII box."""
    yellow = "\033[32m"
    reset = "\033[31m"
    length = len(message)

    print(f"{yellow}+{'-' * (length + 2)}+{reset}")
    print(f"{yellow}| {message} |{reset}")
    print(f"{yellow}+{'-' * (length + 2)}+{reset}")