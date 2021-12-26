from objects.task import Task
import numpy as np

class Result(Task):
    """Wrapper object for a completed class. Holds the initial values and
    the result matrix.

    :param task: Task object which defines the mandlebrot parameters
    :type task: Task
    :param result: the result of the calculations
    :type result: np.matrix
    """
    __slots__ = 'task', 'result'
    
    def __init__(self, task: Task):
        """Constructor
        """
        self.task = task
        self.result = None
