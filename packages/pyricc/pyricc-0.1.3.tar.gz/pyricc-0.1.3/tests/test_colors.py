import unittest
from pyricc import colors

class TestColors(unittest.TestCase):

    def test_to_red(self):
        # Check for the presence of ANSI escape codes.  We don't test the *exact*
        # output, as that can vary slightly between terminals.
        colored_text = colors.to_red("test")
        self.assertIn("\033[91m", colored_text)
        self.assertIn("test", colored_text)
        self.assertIn("\033[0m", colored_text)  # Reset code

    def test_to_green(self):
        colored_text = colors.to_green("test")
        self.assertIn("\033[92m", colored_text)
        self.assertIn("test", colored_text)
        self.assertIn("\033[0m", colored_text)

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            colors._colorize("test", "invalid_color")

    # Add tests for other colors...

if __name__ == '__main__':
    unittest.main()
