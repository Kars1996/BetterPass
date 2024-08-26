# Before we start
This is a super random project, I've been working on relearning python and this was one of the projects I made as I practice python, and I thought I would release it as a pip lib. Sorry if its bad lol I'm still learning, anyway, heres a more "Professional" Readme (Thanks Chatgpt for documentation!)

[!NOTE]
Not on Pypi yet, my email servers are down :sob:
Legit just found out that if u press something lke up key it crashes so i'll add edge cases for that later

# BetterPass 🔒

**BetterPass** is a cross-platform Python library for securely handling password input. With this library, you can prompt users for passwords with custom masking characters while supporting both Windows and Unix-based systems. Perfect for adding a secure input feature to your CLI applications! 

## Features ✨

- **Cross-Platform**: Works on both Windows and Unix-based systems.
- **Custom Masking**: Replace input characters with a custom masking character (e.g., `•`).
- **Backspace Support**: Handle backspaces correctly for user convenience.
- **Keyboard Interrupt Handling**: Gracefully handle Ctrl+C to exit the prompt.

## Installation 🛠️

You can install **BetterPass** via pip:

```bash
pip install betterpass
```

## Usage 📚

Here's a quick example of how to use **BetterPass** in your project:

```python
from betterpass import BetterPass

# Create an instance of BetterPass with a custom masking character
password = BetterPass(char="•")

# Prompt the user for a password
user_input = password.password("Enter your password: ")

print(f"Your password is: {user_input}")
```

## Testing 🧪

You can run the test suite to ensure everything is working correctly:

```bash
python -m unittest discover
```

## Contributing 🤝

If you'd like to contribute to **BetterPass**, feel free to fork the repository and submit a pull request. We welcome improvements and bug fixes!

## License 📜

**BetterPass** is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author 👤

Developed by [Kars](https://kars.bio). For more projects and updates, visit the [author's page](https://kars.bio).
