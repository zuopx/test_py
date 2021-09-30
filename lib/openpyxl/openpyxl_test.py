"""对xlsx文件的读写"""

import unittest
import openpyxl

class TestOpenpyxl(unittest.TestCase):

    def setUp(self):
        self.file = "lib\\openpyxl\\demo.xlsx"
        self.sheetname = "Sheet1"
        self.wb = openpyxl.load_workbook(self.file)
        self.sh = self.wb[self.sheetname]

    def tearDown(self):
        pass

    def testRead(self):
        print(self.wb.sheetnames)
        print(self.sh)
        cell = self.sh["A1"]
        print(cell.value)

    def testWrite(self):
        cell = self.sh["C1"]
        cell.value = 0
        self.wb.save(self.file)


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(TestOpenpyxl("testWrite"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()