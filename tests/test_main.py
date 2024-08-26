import unittest
from betterpass import BetterPass
from unittest.mock import patch


class TestBetterPass(unittest.TestCase):
    @patch("builtins.input", lambda _: "user_password")
    def test_password_unix(self):
        password = BetterPass(char="•")

        # Mocking the input function to simulate a UNIX-based system input
        with patch("platform.system", return_value="Linux"):
            with patch(
                "sys.stdin.read",
                side_effect=[
                    "u",
                    "s",
                    "e",
                    "r",
                    "_",
                    "p",
                    "a",
                    "s",
                    "s",
                    "w",
                    "o",
                    "r",
                    "d",
                    "\n",
                ],
            ):
                result = password.password("Enter your password: ")

        self.assertEqual(result, "user_password")

    @patch(
        "msvcrt.getch",
        side_effect=[
            b"u",
            b"s",
            b"e",
            b"r",
            b"_",
            b"p",
            b"a",
            b"s",
            b"s",
            b"w",
            b"o",
            b"r",
            b"d",
            b"\r",
        ],
    )
    def test_password_windows(self, mock_getch):
        password = BetterPass(char="•")

        # Simulate Windows password input
        with patch("platform.system", return_value="Windows"):
            result = password.password("Enter your password: ")

        self.assertEqual(result, "user_password")

    def test_empty_password(self):
        password = BetterPass(char="•")

        with patch("platform.system", return_value="Linux"):
            with patch("sys.stdin.read", side_effect=["\n"]):
                result = password.password("Enter your password: ")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
