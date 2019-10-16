import unittest
import random

import src.da.problem.sort as sort

class TestSort(unittest.TestCase):

    def setUp(self):
        self.arr = random.sample(range(1000), 200)
        self.sorted_arr = sorted(self.arr)

    @unittest.skip('pass')
    def test_mergesort(self):
        sort.mergesort(self.arr)
        self.assertListEqual(self.arr, self.sorted_arr)

    def test_quicksort(self):
        sort.quicksort(self.arr)
        self.assertListEqual(self.arr, self.sorted_arr)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSort('test_quicksort'))
    suite.addTest(TestSort('test_mergesort'))
    return suite

if __name__ == "__main__":
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())