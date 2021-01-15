import logging

logging.basicConfig(level=logging.INFO)
a_logger = logging.getLogger(__name__)

logging.info('root logger')
a_logger.info('In module a')
from src.python.logging import b

b.func_in_b()