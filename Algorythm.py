import numpy as np
from Taquin import Taquin
import heapq

def algorythm(starting: np.ndarray, SIZE: int) -> list:
    GOAL = np.array([[i + j * SIZE for i in range(1, SIZE + 1)] for j in range(SIZE)])
    GOAL[SIZE - 1][SIZE - 1] = 0
    GOAL_ID = hash(str(GOAL))
    starting = Taquin(0, [], starting, SIZE, GOAL)

    alreadys = set()
    alreadys.add(starting.id)

    to_treat = []
    heapq.heappush(to_treat, (starting.sum, starting))

    complexity_in_time = 0
    max_complexity_in_size = 0

    while to_treat:
        current_sum, current = heapq.heappop(to_treat)
        complexity_in_time += 1
        alreadys.add(current.id)

        if current.get_id(current.matrix) == GOAL_ID:
            return [current.previous + [current], complexity_in_time, max_complexity_in_size]

        for new_matrix in current.get_possible_moves(SIZE, alreadys):
            new_taquin = Taquin(current.previous_distance + 1, current.previous + [current], new_matrix, SIZE, GOAL)
            heapq.heappush(to_treat, (new_taquin.sum, new_taquin))
            max_complexity_in_size = max(max_complexity_in_size, len(to_treat) + len(alreadys))

    return [None, complexity_in_time, max_complexity_in_size]
