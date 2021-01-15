import logging

root = logging.getLogger('')   # 此时，root.handlers为空
root.warning('foo')            # 此时，root.handlers依然为空
logging.warning('foo')         # 此时，root.handlers不为空
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
# logger.addHandler(ch)
# 'application' code
logger.propagate = False
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

print(logger.parent)
print(logger.handlers)