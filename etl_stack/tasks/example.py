from datetime import datetime
from etl_stack.tasks.base import BaseTask


class RandNumTask(BaseTask):

    def extract(self):
        for i in range(self.min_num, self.max_num):
            yield i

    def transform(self, document):
        return document ** 2

    def load(self, document):
        return document
