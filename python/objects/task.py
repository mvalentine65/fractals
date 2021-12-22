

class Task():
    """
    Holds the necessary information for a single worker to perform it's part
    of a larger mandlebrot render.
    
    :param start: highest y-index used in this batch of calculations
    :type start: float
    :param end: lowest y-index used in this batch of calculations
    :type end: float
    :param max_iterations: Maximum number of iterations to calculate before escaping
    :type max_iterations: int
    :param step: increment value for x and y values
    :type step: float
    """
    __slots__ = 'start', 'end', 'max_iterations', 'step'

    def __init__(self, y_start: float, y_end: float, max_iterations: int, step: float):
        """Constructor
        """
        self.start = y_start
        self.end = y_end  # inclusive
        self.max_iterations = max_iterations
        self.step = step

