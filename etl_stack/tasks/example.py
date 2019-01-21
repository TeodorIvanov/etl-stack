from etl_stack.tasks.base import BaseTask


class RandNumTask(BaseTask):

    def extract(self):
        for i in range(self.min_num, self.max_num):
            yield i

    def transform(self, document):
        return document ** 2

    def load(self, document):
        return document


if __name__ == '__main__':
    task = RandNumTask(min_num=0, max_num=100000)
    results = task.execute()
    print(results)
