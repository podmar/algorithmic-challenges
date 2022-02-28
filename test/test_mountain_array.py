import unittest

from challenges.mountain_array import solution

class TestArray(unittest.TestCase): 
    def test_(self): 
        """Testing the solution function to the mountain array challenge
        """

        self.assertEqual(solution([2,1]), False)
        self.assertEqual(solution([3,5,5]), False)
        self.assertEqual(solution([0,3,2,1]), True)
        self.assertEqual(solution([1,2,7,5,2,1]), True)
        self.assertEqual(solution([7,5,3,1,0]), False)
        self.assertEqual(solution([1,5,8,9,17]), False)
        self.assertEqual(solution([1,5,8,9,17,3]), True)
        self.assertEqual(solution([-1,0,1]), False)
        self.assertEqual(solution([-15,-3,0,5,1]), True)
        self.assertEqual(solution([-1,14,20]), False)

if __name__ == "__main__": 
    unittest.main()