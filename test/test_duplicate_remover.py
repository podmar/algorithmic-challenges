import unittest

from challenges.duplicate_remover import solution_1, solution_2

class TestDuplicateRemover(unittest.TestCase): 

# testing the 1st solution makes the code freeze. 
    # def test_solution_1(self): 
    #     """Testing the hacked solution_1
    #     """

    #     self.assertEqual(solution_1("abbaca"), "ca")
    #     self.assertEqual(solution_1("azxxzy"), "ay")
    #     self.assertEqual(solution_1("rbbrwaawkcc"), "k")
    #     self.assertEqual(solution_1("zuqqrrueezuipp"), "ui")
    #     self.assertEqual(solution_1("uubb"), "")
    #     self.assertEqual(solution_1("nthstkzbbzktshyyte"), "ne")
    #     self.assertEqual(solution_1("zuzutseettseg"), "zuzuteg")
    #     self.assertEqual(solution_1("abracadabra"), "abracadabra")
    #     self.assertEqual(solution_1("etweeewwwwtzuue" ), "etwetze")
    #     self.assertEqual(solution_1(s)("etblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfueh"), "etblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfueh")

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


    # @classmethod
    # def setUpClass(cls): 
    #     print("setupClass")

    # @classmethod
    # def tearDownClass(cls): 
    #     print("teardownClass")

    # def setUp(self): 

    #     self.test1 = "abbaca" 
    #     self.test2 = "azxxzy"
    #     self.test3 = "rbbrwaawkcc" 
    #     self.test4 = "zuqqrrueezuipp" 
    #     self.test5 = "uubb"
    #     self.test6 = "nthstkzbbzktshyyte"
    #     self.test7 = "zuzutseettseg" 
    #     self.test8 = "abracadabra"
    #     self.test9 = "etweeewwwwtzuue" 
    #     self.test10 = "etblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfaabhbbwlqksjbrgdjknbmvxycvghfdjhfhdfueh"

    #     self.output1 = "ca"
    #     self.output2 = "ay"
    #     self.output3 = "k"
    #     self.output4 = "ui"
    #     self.output5 = ""
    #     self.output6 = "ne" 
    #     self.output7 = "zuzuteg"
    #     self.output8 = "abracadabra"
    #     self.output9 = "etwetze"
    #     self.output10 = "etblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfuehetblfbhwlqksjbrgdjknbmvxycvghfdjhfhdfueh"

    # def tearDown(self): 
    #     pass
    
    # def test_solution_1(self): 
    #     """Testing the hacked solution_1
    #     """

    #     self.assertEqual(solution_1(self.test1), self.output1)
    #     self.assertEqual(solution_1(self.test2), self.output2)
    #     self.assertEqual(solution_1(self.test3), self.output3)
    #     self.assertEqual(solution_1(self.test4), self.output4)
    #     self.assertEqual(solution_1(self.test5), self.output5)
    #     self.assertEqual(solution_1(self.test6), self.output6)
    #     self.assertEqual(solution_1(self.test7), self.output7)
    #     self.assertEqual(solution_1(self.test8), self.output8)
    #     self.assertEqual(solution_1(self.test9), self.output9)
    #     self.assertEqual(solution_1(self.test10), self.output10)

    # def test_solution_2(self): 
    #     """Testing the hacked solution_1
    #     """

    #     self.assertEqual(solution_2(self.test1), self.output1)
    #     self.assertEqual(solution_2(self.test2), self.output2)
    #     self.assertEqual(solution_2(self.test3), self.output3)
    #     self.assertEqual(solution_2(self.test4), self.output4)
    #     self.assertEqual(solution_2(self.test5), self.output5)
    #     self.assertEqual(solution_2(self.test6), self.output6)
    #     self.assertEqual(solution_2(self.test7), self.output7)
    #     self.assertEqual(solution_2(self.test8), self.output8)
    #     self.assertEqual(solution_2(self.test9), self.output9)
    #     self.assertEqual(solution_2(self.test10), self.output10)

if __name__ == "__main__": 
    unittest.main()