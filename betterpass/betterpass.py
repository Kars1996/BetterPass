# region BetterClass
# Classed version of betterpass
# NOTE Chatgpt made the docs

import sys
import platform


class BetterPass:
    """
    A class for handling password input in a cross-platform manner.

    The BetterPass class provides methods for accepting password input from the user
    while replacing the actual characters with a custom character (e.g., `•`).

    Attributes:
    -----------
    char : str
        The character used to mask the password input. Defaults to `•`.

    Methods:
    --------
    password(text: str) -> str:
        Prompts the user for a password, masking input using the specified `char`.
        Determines the appropriate method based on the operating system.

    _windows_password(text: str) -> str:
        Handles password input on Windows systems using the `msvcrt` library.
        Characters are replaced by `char`, and backspace support is provided.

    _unix_password(text: str) -> str:
        Handles password input on Unix-based systems using the `termios` and `tty` libraries.
        Characters are replaced by `char`, and backspace support is provided.
    """

    def __init__(self, char: str = "•") -> None:
        """
        Initializes the BetterPass class with the masking character set to `•`.
        """
        self.char: str = char  # Char to replace input with

    def password(self, text: str) -> str:
        """
        Prompts the user for a password, masking input using the `char` attribute.

        Parameters:
        -----------
        text : str
            The prompt text to display before taking input.

        Returns:
        --------
        str
            The password input entered by the user.
        """
        print(text, end="")
        sys.stdout.flush()  # Ensure the prompt is shown immediately
        if platform.system() == "Windows":
            return self._windows_password()
        else:
            return self._unix_password()

    def _windows_password(self) -> str:
        """
        Handles password input on Windows systems using the `msvcrt` library.

        Parameters:
        -----------
        text : str
            The prompt text to display before taking input.

        Returns:
        --------
        str
            The password input entered by the user.
        """
        import msvcrt

        password = []
        while True:
            char = msvcrt.getch()
            if char in {b"\r", b"\n"}:
                break
            elif char == b"\x03":  # Ctrl+C
                raise KeyboardInterrupt()
            elif char == b"\x08":  # Backspace
                if password:
                    password.pop()
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            else:
                password.append(char.decode("utf-8"))
                sys.stdout.write(self.char)
                sys.stdout.flush()
        sys.stdout.write("\n")
        return "".join(password) if password else None

    def _unix_password(self) -> str:
        """
        Handles password input on Unix-based systems using the `termios` and `tty` libraries.

        Parameters:
        -----------
        text : str
            The prompt text to display before taking input.

        Returns:
        --------
        str
            The password input entered by the user.
        """
        import termios
        import tty

        password = []

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        tty.setraw(fd)
        try:
            while True:
                char = sys.stdin.read(1)
                if char == "\n":
                    break
                elif char == "\x03":  # Ctrl+C
                    raise KeyboardInterrupt()
                elif char == "\x7f":  # Backspace
                    if password:
                        password.pop()
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                else:
                    password.append(char)
                    sys.stdout.write(self.char)
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        sys.stdout.write("\n")
        return "".join(password) if password else None