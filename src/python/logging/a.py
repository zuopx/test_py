import logging

a_logger = logging.getLogger(__name__)

logging.warning('root logger')
a_logger.warning('In module a')
from src.python.logging import b

b.func_in_b()