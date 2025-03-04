""""""
import unittest
import logging

logging.basicConfig(level=logging.INFO)  # 默认为rootLogger添加StreamHanlder


class TestHandler(unittest.TestCase):
    name = "log.log"

    def test_handler(self):
        logger = logging.getLogger(self.name)

        logger.addHandler(logging.FileHandler(f"{self.name}.log", "a"))

        logger.info("test")


class TestParent(unittest.TestCase):
    def test_parent(self):
        ab = logging.getLogger("a.b")
        a = logging.getLogger("a")

        self.assertIs(ab.parent, a)
        self.assertIs(a.parent, logging.root)

        ab.info("test")

        self.assertFalse(ab.handlers)
        self.assertTrue(ab.hasHandlers())  # ab不持有handler，使用祖类rootLogger的handler


class TestFilter(unittest.TestCase):
    def test_filter(self):
        h = logging.StreamHandler()
        h.addFilter(logging.Filter("a"))  # h只为a服务

        a = logging.getLogger("a")
        b = logging.getLogger("b")
        a.addHandler(h)
        b.addHandler(h)

        a.info("a-test")
        b.info("b-test")


class TestFormat(unittest.TestCase):
    def test_format(self):
        """format

        %(name)s            Name of the logger (logging channel)
        %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                            WARNING, ERROR, CRITICAL)
        %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                            "WARNING", "ERROR", "CRITICAL")
        %(pathname)s        Full pathname of the source file where the logging
                            call was issued (if available)
        %(filename)s        Filename portion of pathname
        %(module)s          Module (name portion of filename)
        %(lineno)d          Source line number where the logging call was issued
                            (if available)
        %(funcName)s        Function name
        %(created)f         Time when the LogRecord was created (time.time()
                            return value)
        %(asctime)s         Textual time when the LogRecord was created
        %(msecs)d           Millisecond portion of the creation time
        %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                            relative to the time the logging module was loaded
                            (typically at application startup time)
        %(thread)d          Thread ID (if available)
        %(threadName)s      Thread name (if available)
        %(taskName)s        Task name (if available)
        %(process)d         Process ID (if available)
        %(message)s         The result of record.getMessage(), computed just as
                            the record is emitted
        """
        a = logging.getLogger("a")
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(asctime)s %(name)s-%(levelname)s-%(message)s", "%Y-%m-%d %H:%M:%S"))
        a.addHandler(h)

        a.info("test")


if __name__ == "__main__":
    unittest.main()
