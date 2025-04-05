from .._progress import TqdmProgressManager

class UnregisterProgress:

    def __init__(self,task_id:int):
        self.task_id = task_id

    def __call__(self,future):
        TqdmProgressManager.unregister(self.task_id)
