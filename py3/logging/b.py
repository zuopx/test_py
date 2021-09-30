import logging

b_logger = logging.getLogger(__name__)

def func_in_b():
    b_logger.warning('In function func_in_b')