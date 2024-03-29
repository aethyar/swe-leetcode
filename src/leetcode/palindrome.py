# palindrome.py


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower()  # Convert string to lowercase for case-insensitive comparison
    # Remove non-alphanumeric characters
    s = "".join(char for char in s if char.isalnum())
    return s == s[::-1]
