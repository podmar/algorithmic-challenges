import unittest

from challenges.mountain_array import solution

class TestArray(unittest.TestCase): 
    def test_(self): 
        """Testing the solution function to the mountain array challenge
        """
        self.assertFalse(solution([2,1]))
        self.assertFalse(solution([3,5,5]))
        self.assertTrue(solution([0,3,2,1]))
        self.assertTrue(solution([1,2,7,5,2,1]))
        self.assertFalse(solution([7,5,3,1,0]))
        self.assertFalse(solution([1,5,8,9,17]))
        self.assertTrue(solution([1,5,8,9,17,3]))
        self.assertFalse(solution([-1,0,1]))
        self.assertTrue(solution([-15,-3,0,5,1]))
        self.assertFalse(solution([-1,14,20]))

if __name__ == "__main__": 
    unittest.main()