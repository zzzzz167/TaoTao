from abc import ABC, abstractmethod
import logging
import datetime

#AbstractLogger类的实现
class AbstractLogger(ABC):
    @abstractmethod
    def info(self, msg):
        pass

    @abstractmethod
    def error(self, msg):
        pass

    @abstractmethod
    def debug(self, msg):
        pass

    @abstractmethod
    def warn(self, msg):
        pass

    @abstractmethod
    def exception(self, msg):
        pass##

#日志输出类
class CustomLogger(AbstractLogger):
    def __init__(self, **kwargs) -> None:
        # logging.basicConfig(format='[%(asctime)s][%(levelname)s]: %(message)s', level=\
        #    logging.INFO if not kwargs.get("debug") else logging.DEBUG)
        #日志向文件输出
        fh = logging.FileHandler('log/{}.log'.format(datetime.datetime.strftime(datetime.datetime.now(),'%F')),encoding='utf-8')
        fh.setFormatter(logging.Formatter("[%(asctime)s][%(levelname)s]: %(message)s"))
        logging.basicConfig(
            format="[%(asctime)s][%(levelname)s]: %(message)s",
            level=logging.DEBUG,
            #filename='log/{}.log'.format(datetime.datetime.strftime(datetime.datetime.now(),'%F')),
        )
        logging.getLogger('').addHandler(fh)
        '''
        #日志控制台打印
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        '''

    def info(self, msg):
        return logging.info(msg)

    def error(self, msg):
        return logging.error(msg)

    def debug(self, msg):
        return logging.debug(msg)

    def warn(self, msg):
        return logging.warn(msg)

    def exception(self, msg):
        return logging.exception(msg)
