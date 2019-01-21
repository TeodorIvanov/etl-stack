import logging
from datetime import datetime

from abc import ABC, abstractmethod

from etl_stack import settings


class BaseTask(ABC):

    def __init__(self, executor=None, **kwargs):
        self.kwargs = kwargs
        if executor is not None:
            self.executor = executor
        else:
            self.executor = settings.DEFAULT_EXECUTOR

        for kwarg_key, kwarg_val in kwargs.items():
            setattr(self, kwarg_key, kwarg_val)
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.logger = self.get_logger()

    def on_extract_start(self):
        self.start_time = datetime.now()
        self.logger.info('Extracting documents')

    @abstractmethod
    def extract(self, document):
        pass

    def on_transform_start(self, documents):
        self.logger.info('Transforming %s documents', len(documents))

    @abstractmethod
    def transform(self, document):
        pass

    def on_load_start(self, documents):
        self.logger.info('Loading %s documents', len(documents))

    @abstractmethod
    def load(self, document):
        pass

    def on_task_done(self, documents):
        self.end_time = datetime.now()
        self.duration = self.end_time - self.start_time
        self.logger.info('Task is done')
        self.logger.info('Processed %s in %s', len(documents), self.duration)


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
        logger.setLevel(log_level)
        formatter = logging.Formatter(
            '%(asctime)s [%(task_name)s]: %(message)s')
        syslog.setFormatter(formatter)
        logger.addHandler(syslog)
        logger = logging.LoggerAdapter(logger, extra)
        return logger
