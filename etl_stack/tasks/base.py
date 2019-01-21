import logging

from abc import ABC, abstractmethod

from etl_stack import settings


class BaseTask(ABC):

    def __init__(self, executor=None, *args, **kwargs):
        self.kwargs = kwargs
        if executor is not None:
            self.executor = executor
        else:
            self.executor = settings.DEFAULT_EXECUTOR

        for kwarg_key, kwarg_val in kwargs.items():
            setattr(self, kwarg_key, kwarg_val)

        self.logger = self.get_logger()

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass

    def execute(self, **kwargs):
        self.executor(task=self, **kwargs).execute()

    def get_logger(self):
        task_name = self.__class__.__name__
        extra = {
            'task_name': task_name,
        }
        syslog = logging.StreamHandler()
        logger = logging.getLogger(self.__class__.__name__)
        # Reset the logger.handlers if it already exists.
        if logger.handlers:
            logger.handlers = []
        log_level = getattr(logging, settings.LOG_LEVEL, logging.INFO)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s [%(task_name)s]: %(message)s')
        syslog.setFormatter(formatter)
        logger.addHandler(syslog)
        logger = logging.LoggerAdapter(logger, extra)
        return logger
