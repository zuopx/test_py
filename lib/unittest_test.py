""""""
import unittest


class TestExample(unittest.TestCase):
    def testExample(self):
        print("testExample")


class TestUnittest(unittest.TestCase):
    def testCase(self):
        with self.assertRaises(ValueError):
            case = TestExample("wrongName")

        case = TestExample("testExample")
        self.assertTrue(callable(case), "TestCase instance must be callable.")

    def testSuite(self):
        suite = unittest.TestSuite()
        self.assertTrue(callable(suite), "TestSuite instance must be callable.")

        case = TestExample("testExample")
        suite.addTest(case)
        self.assertIn(case, suite._tests)


if __name__ == "__main__":
    unittest.main(defaultTest="TestUnittest")
