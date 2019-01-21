### etl-stack ###

**work in progress**


A bare-minimum ETL framework using joblib (or anything you want)

- Build class-based multithreaded ETL pipelines in Python
- Achieve amazing performance by using [joblib](https://joblib.readthedocs.io/)
- Get beautiful progress logs thanks to [tqdm](https://pypi.org/project/tqdm/)
- Write your own job executors to satisfy threading or multiprocessing nees

##### Example #####

```
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
```
