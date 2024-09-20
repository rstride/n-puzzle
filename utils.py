import numpy as np
from Taquin import Taquin
import settings

def print_list(taquins:list):
    print("List of effectued moves :\n")
    for i in range(0, len(taquins), 10):
        for j in range(len(taquins[i].matrix)):
            for k in range(i, min(i + 10, len(taquins))):
                print(taquins[k].matrix[j], end=" ")
            print()
        if i + 10 < len(taquins):
            print('\n')

def count_inversions(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and arr[i] != 0 and arr[j] != 0:
                inv_count += 1
    return inv_count

def is_solvable(puzzle):
    flattened_puzzle = puzzle.flatten()
    inversions = count_inversions(flattened_puzzle)
    size = puzzle.shape[0]
    if size % 2 != 0:
        return inversions % 2 == 0
    else:
        row_from_bottom = size - np.where(puzzle == 0)[0][0]
        return (row_from_bottom % 2 != 0) == (inversions % 2 == 0)
