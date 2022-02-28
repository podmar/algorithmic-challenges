import unittest

from challenges.palindrome_number import string_solution, log10_solution, modulo_solution

class TestPalindrome(unittest.TestCase): 
    def test_string_solution(self): 
        """Testing the first solution with string approach
        """

        self.assertEqual(string_solution(121), True)
        self.assertEqual(string_solution(-121), False)
        self.assertEqual(string_solution(123), False)
        self.assertEqual(string_solution(-2), False)
        self.assertEqual(string_solution(10455401), True)
        self.assertEqual(string_solution(0), True)
        self.assertEqual(string_solution(50895), False)
        self.assertEqual(string_solution(44444), True)

    def test_log10_solution(self): 
        """Testing the solution with log10
        """

        self.assertEqual(log10_solution(121), True)
        self.assertEqual(log10_solution(-121), False)
        self.assertEqual(log10_solution(123), False)
        self.assertEqual(log10_solution(-2), False)
        self.assertEqual(log10_solution(10455401), True)
        self.assertEqual(log10_solution(0), True)
        self.assertEqual(log10_solution(50895), False)
        self.assertEqual(log10_solution(44444), True)

    def test_modulo_solution(self): 
        """Testing the modulo solution
        """

        self.assertEqual(modulo_solution(121), True)
        self.assertEqual(modulo_solution(-121), False)
        self.assertEqual(modulo_solution(123), False)
        self.assertEqual(modulo_solution(-2), False)
        self.assertEqual(modulo_solution(10455401), True)
        self.assertEqual(modulo_solution(0), True)
        self.assertEqual(modulo_solution(50895), False)
        self.assertEqual(modulo_solution(44444), True)


if __name__ == "__main__": 
    unittest.main()