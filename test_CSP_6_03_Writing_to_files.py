import unittest
import os

from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore


class TestFileLab(unittest.TestCase):

    def setUp(self):
        """Clean slate before each test."""
        self.files = ["names.txt", "namesNew.txt", "scores.txt"]
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def tearDown(self):
        """Clean up after each test."""
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def test_01_writeFile(self):
        """Verifies writeFile creates a file with one list item per line."""
        test_list = ["Python", "Java", "C++"]
        writeFile(test_list, "names.txt")

        self.assertTrue(os.path.exists("names.txt"), "writeFile should create names.txt")
        with open("names.txt", "r") as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(lines, test_list)

    def test_02_sortNames(self):
        """Verifies names are read from one file, sorted, and saved to another."""
        unsorted = ["Zebra", "Apple", "Monkey"]
        with open("names.txt", "w") as f:
            for item in unsorted:
                f.write(f"{item}\n")

        sortNames("names.txt", "namesNew.txt")

        self.assertTrue(os.path.exists("namesNew.txt"))
        with open("namesNew.txt", "r") as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(lines, ["Apple", "Monkey", "Zebra"])

    def test_03_highScore_average(self):
        """Verifies highScore adds to the file and returns the correct average."""
        with open("scores.txt", "w") as f:
            f.write("10\n20\n")

        avg = highScore(60)

        self.assertEqual(avg, 30.0, "The average should be 30.0")

        with open("scores.txt", "r") as f:
            content = f.read()
        self.assertIn("60", content, "The new score 60 must be saved in the file.")


if __name__ == "__main__":
    unittest.main()