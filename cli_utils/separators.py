# cli_utils/separators.py

def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_custom_separator(char, length):
    print(char * int(length))

def print_box(message, char="*"):
    length = len(message) + 4
    print(char * length)
    print(f"{char} {message} {char}")
    print(char * length)