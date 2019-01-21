from joblib import Parallel, delayed
from tqdm import tqdm

from etl_stack.executors.base import BaseExecutor


class JobLibExecutor(BaseExecutor):

    def execute(self):
        lazy_transforms = [
            delayed(self.task.transform)(document)
            for document in tqdm(self.task.extract())
        ]
        self.task.on_transform_start()

        transformed = Parallel(n_jobs=self.workers)(tqdm(lazy_transforms))

        self.task.on_load_start()
        loaded = Parallel(n_jobs=self.workers)(
            delayed(self.task.load)(document)
            for document in tqdm(transformed)
        )
        self.task.on_task_done(loaded)
        return loaded
