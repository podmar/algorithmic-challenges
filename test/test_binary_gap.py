import unittest

# target = __import__("binary_gap.py")
# solution = target.solution

from challenges.binary_gap import solution

class TestGap(unittest.TestCase): 
    def test_gap_length(self): 
        """Testing the lenght of the gap
        """

        self.assertEqual(solution(2), 0)
        self.assertEqual(solution(5), 1) #5 = 0b101
        self.assertEqual(solution(45), 1) #45 = 0b101101
        self.assertEqual(solution(1793), 7) #1793 = 0b11100000001
        self.assertEqual(solution(2049), 10) #2049 = 0b100000000001

    def test_multiple_gaps(self):
        """Testing cases with multiple gaps
        """

        self.assertEqual(solution(1089), 5) #1089= 0b10001000001
        self.assertEqual(solution(26394799112193), 20) #1319739955609 = 0b110000000000110000100101000000000000000000001

    def test_end_0(self): 
        """Testing with "0" at the end
        """

        self.assertEqual(solution(13197399556096), 10) #1319739955609 = 0b11000000000011000010010100000000000000000000
        self.assertEqual(solution(144), 2) #144 = 0b10010000
    
    def test_negative(self): 
        """Testing negative numbers
        """

        self.assertEqual(solution(-2), 0)
        self.assertEqual(solution(-5), 1) #5 = 0b101
        self.assertEqual(solution(-45), 1) #45 = 0b101101

if __name__ == "__main__": 
    unittest.main()