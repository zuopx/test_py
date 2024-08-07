"""配置解析"""
import configparser
import unittest


class TestConfigParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = configparser.ConfigParser()
        cls.config.read("lib\\configparser\\config.ini")

    def testRead(self):
        self.assertEqual("g68", self.config["mongo"]["user"])
        self.assertEqual("gameg68!#", self.config["mongo"]["password"])
        self.assertEqual("128", self.config["redis"].get("poolsize"))

    def testTypeConvert(self):
        self.assertEqual(128, self.config["redis"].getint("poolsize"))
        self.assertEqual(True, self.config.getboolean("rank", "state"))


if __name__ == "__main__":
    unittest.main()
