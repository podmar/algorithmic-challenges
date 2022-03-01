import unittest

from challenges.palindrome_number import string_solution, log10_solution, modulo_solution

class TestPalindrome(unittest.TestCase): 
    def test_string_solution(self): 
        """Testing the first solution with string approach
        """

        self.assertTrue(string_solution(121))
        self.assertFalse(string_solution(-121))
        self.assertFalse(string_solution(123))
        self.assertFalse(string_solution(-2))
        self.assertTrue(string_solution(10455401))
        self.assertTrue(string_solution(0))
        self.assertFalse(string_solution(50895))
        self.assertTrue(string_solution(44444))

    def test_log10_solution(self): 
        """Testing the solution with log10
        """

        self.assertTrue(log10_solution(121))
        self.assertFalse(log10_solution(-121))
        self.assertFalse(log10_solution(123))
        self.assertFalse(log10_solution(-2))
        self.assertTrue(log10_solution(10455401))
        self.assertTrue(log10_solution(0))
        self.assertFalse(log10_solution(50895))
        self.assertTrue(log10_solution(44444))

    def test_modulo_solution(self): 
        """Testing the modulo solution
        """

        self.assertTrue(modulo_solution(121))
        self.assertFalse(modulo_solution(-121))
        self.assertFalse(modulo_solution(123))
        self.assertFalse(modulo_solution(-2))
        self.assertTrue(modulo_solution(10455401))
        self.assertTrue(modulo_solution(0))
        self.assertFalse(modulo_solution(50895))
        self.assertTrue(modulo_solution(44444))


if __name__ == "__main__": 
    unittest.main()