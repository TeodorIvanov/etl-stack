from abc import ABC, abstractmethod

from etl_stack import settings


class BaseExecutor(ABC):

    def __init__(self, task, workers=None):
        self.task = task
        if workers is None:
            self.workers = settings.WORKERS
        else:
            self.workers = workers
