import logging
logger = logging.getLogger('test')
# logging.basicConfig()  # basicConfig是logging提供的简单的配置方法，不用basicConfig则需要手动添加handler
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.INFO)
fmt = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')
file_handler.setFormatter(fmt)
logger.addHandler(file_handler)


logger.setLevel(logging.DEBUG)  # 输出所有大于等于INFO级别的log
logger.warning('warning')
logger.info('I am <info> message.')
logger.debug('I am <debug> message.')  # 不输出



print(logger.handlers)