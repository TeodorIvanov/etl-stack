from etl_stack.tasks.base import BaseTask


class RandNumTask(BaseTask):

    def extract(self):
        self.logger.info('Extracting documents')
        for i in range(self.min_num, self.max_num):
            yield i

    def on_transform_start(self):
        self.logger.info('Transforming documents')

    def transform(self, document):
        return document ** 2

    def on_load_start(self):
        self.logger.info('Loading documents')

    def load(self, document):
        return document

    def on_task_done(self, loaded):
        self.logger.info('Task is done')
        self.logger.info('Wow, we did %s calculations', len(loaded))
