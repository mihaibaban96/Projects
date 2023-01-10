import unittest
import script_1


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script_1.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script_1.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_out_of_range_numers(self):
        result = script_1.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_string(self):
        result = script_1.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
