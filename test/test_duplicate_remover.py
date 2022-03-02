import unittest

from challenges.duplicate_remover import solution_1, solution_2

class TestDuplicateRemover(unittest.TestCase): 

#testing the 1st solution makes the code freeze. 
    def test_solution_1(self): 
        """Testing the hacked solution_1
        """

        self.assertEqual(solution_1("abbaca"), "ca")
        self.assertEqual(solution_1("azxxzy"), "ay")
        self.assertEqual(solution_1("rbbrwaawkcc"), "k")
        self.assertEqual(solution_1("zuqqrrueezuipp"), "ui")
        self.assertEqual(solution_1("uubb"), "")
        self.assertEqual(solution_1("nthstkzbbzktshyyte"), "ne")
        self.assertEqual(solution_1("zuzutseettseg"), "zuzuteg")
        self.assertEqual(solution_1("abracadabra"), "abracadabra")
        self.assertEqual(solution_1("etweeewwwwtzuue" ), "etwetze")
        self.assertEqual(solution_1("etblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfueh"), "etblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfueh")
    
    def test_solution_2(self): 
        """Testing the second proper solution
        """

        self.assertEqual(solution_2("abbaca"), "ca")
        self.assertEqual(solution_2("azxxzy"), "ay")
        self.assertEqual(solution_2("rbbrwaawkcc"), "k")
        self.assertEqual(solution_2("zuqqrrueezuipp"), "ui")
        self.assertEqual(solution_2("uubb"), "")
        self.assertEqual(solution_2("nthstkzbbzktshyyte"), "ne")
        self.assertEqual(solution_2("zuzutseettseg"), "zuzuteg")
        self.assertEqual(solution_2("abracadabra"), "abracadabra")
        self.assertEqual(solution_2("etweeewwwwtzuue" ), "etwetze")
        self.assertEqual(solution_2("etblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfueh"), "etblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfueh")

if __name__ == "__main__": 
    unittest.main()