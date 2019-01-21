from joblib import Parallel, delayed
from tqdm import tqdm

from etl_stack.executors.base import BaseExecutor


class JobLibExecutor(BaseExecutor):

    def get_extracted(self):
        return [
            delayed(self.task.transform)(document)
            for document in tqdm(self.task.extract())
        ]

    def get_transformed(self, documents):
        return Parallel(n_jobs=self.workers)(tqdm(documents))

    def get_loaded(self, transformed):
        return Parallel(n_jobs=self.workers)(
            delayed(self.task.load)(document)
            for document in tqdm(transformed)
        )
