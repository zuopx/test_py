"""unittest

python -m unittest -h

Examples:
  python -m unittest test_module               - run tests from test_module
  python -m unittest module.TestClass          - run tests from module.TestClass
  python -m unittest module.Class.test_method  - run specified test method
  python -m unittest path/to/test_file.py      - run tests from test_file.py

测试类下面测试方法的执行顺序：字典顺序
"""
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


class TestHook(unittest.TestCase):
    """test hook

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        pass

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        pass

    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class fixture before running tests in the class."

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
    """

    def setUp(self):
        print("set up")

    def tearDown(self) -> None:
        print("tear down")
        return super().tearDown()

    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")
        return super().tearDownClass()

    def testCase1(self):
        pass

    def testCase2(self):
        pass


if __name__ == "__main__":
    unittest.main(defaultTest="TestHook")
