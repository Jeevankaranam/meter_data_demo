import unittest
from unittest.mock import patch

from src.main import main


class TestMain(unittest.TestCase):
    @patch("builtins.print")
    def test_main(_, mock_print):
        main()
        mock_print.assert_called_with("hello world!")


if __name__ == "__main__":
    unittest.main()
