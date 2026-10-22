import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "checker"))
import straight_check as sc  # noqa: E402

GOOD = "It is a way for two programs to talk. Think of a waiter. You say what you want. The waiter brings it. Want an example?"
BAD = ("Great question! An API is simply a set of protocols and tools for building software, and obviously you should initialize the "
       "configuration parameter before you instantiate the repository directory, which will validate the dependency architecture.")


class T(unittest.TestCase):
    def test_good_is_easy(self):
        r = sc.check(GOOD)
        self.assertEqual(r["notes"], [])
        self.assertLessEqual(r["grade"], 8)

    def test_bad_is_flagged(self):
        r = sc.check(BAD)
        text = " ".join(r["notes"])
        self.assertIn("Great question", text.title().replace("Great Question", "Great question"))
        self.assertIn("simply", text)
        self.assertIn("obviously", text)
        self.assertIn("Hard words", text)
        self.assertLess(r["score"], 70)

    def test_code_blocks_ignored(self):
        r = sc.check("Run this.\n```\nthis is a very long line of code that is not prose at all and should not count against the writer\n```\nThen wait.")
        self.assertEqual(r["notes"], [])

    def test_syllables(self):
        self.assertEqual(sc.syllables("make"), 1)
        self.assertEqual(sc.syllables("folder"), 2)
        self.assertGreaterEqual(sc.syllables("configuration"), 4)


if __name__ == "__main__":
    unittest.main()
