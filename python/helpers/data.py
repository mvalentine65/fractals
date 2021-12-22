"""
Utility functions for making the data matrix.
"""
import numpy as np


def find_length(step: float) -> int:
    """Finds the number of steps needed to cover -2 to 2, the entire length of
    the mandlebrot graph. Takes the increment value as a float, returns the result
    as a int."""
    MAX_DISTANCE = 4
    length = int(MAX_DISTANCE/step) + 1
    return length


def make_matrix(step=0.025) -> np.ndarray:
    """Makes a 2d numpy array. Each value represents one point of data
    in the final graph."""
    length = find_length(step)
    shape = (length, length)
    matrix = np.zeros(shape)
    return matrix


def y_index(matrix: np.matrix, step=0.025) -> None:
    """Iterates over a 2d numpy array and sets the values in each row to the
    appropriate y-value. This preserves the imaginary component of each location
    during the Pool iteration."""
    height = len(matrix)
    for y in range(height):
        matrix[y][0] = 2 - (y*step)


def find_delta(step: float, index: int) -> float:
    """Multiples the step value by the index value to find the total change."""
    result = step * index
    return result

     
def find_real_component(step: float, index: int) -> float:
    """Finds the real component of the complex number C. Takes the step
    and index in the numpy matrix as arguments. Returns the real component
    as a float."""
    X_START = -2
    delta = find_delta(step, index)
    result = X_START + delta
    return result

    
def find_imaginary_component(step: float, index: int) -> float:
    """Finds the imaginary component of the complex number C. Takes the step
    and index in the numpy matrix as arguments. Returns the imaginary component
    as a float."""
    Y_START = 2
    delta = find_delta(step, index)
    result = Y_START - delta
    return result

