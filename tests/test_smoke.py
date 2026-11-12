import unittest

from durations.parse import parse_duration


class SmokeTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2m"), 120)
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1h2m3s"), 3723)

    def test_invalid(self):
        for bad in ["", "10", "5x"]:
            with self.assertRaises(ValueError):
                parse_duration(bad)


if __name__ == "__main__":
    unittest.main()
