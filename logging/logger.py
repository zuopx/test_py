"""创建一个全局logger"""
import logging
import datetime

logger = None


def InitLogger():
    global logger
    if logger is not None:
        return

    logging.basicConfig(
        handlers=[logging.StreamHandler(), logging.FileHandler(f"{datetime.date.today()}.log", "a")],
        format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        level=logging.DEBUG
    )

    logger = logging.getLogger()
    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(f"{datetime.date.today()}.log", "a")
    logger.addHandler(handler1)
    logger.addHandler(handler2)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.DEBUG)
    handler2.setLevel(logging.INFO)

    logger.info("InitLogger Success.")


InitLogger()
