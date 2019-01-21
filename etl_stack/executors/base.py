from abc import ABC, abstractmethod

from etl_stack import settings


class BaseExecutor(ABC):

    def __init__(self, task, workers=None):
        self.task = task
        if workers is None:
            self.workers = settings.WORKERS
        else:
            self.workers = workers

    @abstractmethod
    def get_extracted(self):
        pass

    @abstractmethod
    def get_transformed(self, documents):
        pass

    @abstractmethod
    def get_loaded(self, documents):
        pass

    def execute(self):
        self.task.on_extract_start()
        documents = self.get_extracted()
        self.task.on_transform_start(documents)
        transformed = self.get_transformed(documents)
        self.task.on_load_start(transformed)
        loaded = self.get_loaded(transformed)
        self.task.on_task_done(loaded)
        return loaded
