import logging
import traceback


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("测试日志")
        self.logger.setLevel(logging.DEBUG)

        # 创建handler
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('C:/Users/Hasee/PycharmProjects/pythonProjectForWork/interfaceAutomationTest/log/test.log')

        stream_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        # 定义输出格式
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


def getlog():
    return Logger().logger


# logger.info('this is a info')
# logger.warning('this is a warning')
# logger.debug('this is a debug')

def onedome():
    a = 1
    assert a == 2


