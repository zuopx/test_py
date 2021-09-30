"""时间计算和显示"""

import unittest
import datetime


class TestDatatime(unittest.TestCase):
    def setUp(self) -> None:
        self.tzinfo = datetime.timezone(datetime.timedelta(hours=8))        

    def tearDown(self) -> None:
        return super().tearDown()

    def testGetTime(self):
        """显示时间"""
        now = datetime.datetime.now()
        print(now)

    def testStrptime(self):
        """str -> time"""
        s = "2021:09:28 15:21:23"
        t = datetime.datetime.strptime(s, "%Y:%m:%d %H:%M:%S")
        print(t)

    def testStrftime(self):
        """time -> str"""
        now = datetime.datetime.now()
        s = now.strftime("%Y:%m:%d %H:%M:%S")
        print(s)

    def testTimeStamp(self):
        """时间戳
        
        timestamp()
        fromtimestamp()
        """
        now = datetime.datetime.now()
        ts = now.timestamp()
        print(datetime.datetime.fromtimestamp(ts))

    def testGetTimeDelta(self):
        """显示时间间隔"""
        pass

    def testGetWeekday(self):
        """显示星期几"""
        pass


if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDatatime))
