import numpy as np
from Heuristique import choose_heuristic

class Taquin:
    """
    Taquin class
    """

    def __init__(self, previous_distance:int, previous:list, matrix:np.ndarray, SIZE:int, GOAL:np.ndarray):
        self.matrix = matrix
        self.previous_distance = previous_distance
        self.previous = previous
        self.heuristic = self.calcul_heuristic(SIZE, GOAL)
        self.sum = self.heuristic + self.previous_distance
        self.id = hash(str(matrix))

    def __lt__(self, other):
        return self.sum < other.sum

    def __str__(self):
        return str(self.matrix) + '\n'

    def __repr__(self):
        return str(self.matrix)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Taquin):
            return self.id == other.id
        else:
            return super().__eq__(other)

    def get_id(self, matrix:np.ndarray) -> int:
        return hash(str(matrix))

    def calcul_heuristic(self, SIZE:int, GOAL:np.ndarray) -> int:
        return choose_heuristic(self.matrix, SIZE, GOAL)

    def after_move(self, move:tuple, zero:tuple) -> np.ndarray:
        """
        Return a new matrix after a move
        """
        new_matrix = np.copy(self.matrix)
        new_matrix[move[0]][move[1]], new_matrix[zero[0], zero[1]] = new_matrix[zero[0], zero[1]], new_matrix[move[0]][move[1]]
        return new_matrix

    def get_possible_moves(self, SIZE:int, alreadys:set) -> list:
        new_matrixes = []
        i, j = np.where(self.matrix == 0)[0][0], np.where(self.matrix == 0)[1][0]
        if i > 0:
            new_matrix = self.after_move((i - 1, j), (i, j))
            if self.get_id(new_matrix) not in alreadys:
                new_matrixes.append(new_matrix)
        if i < SIZE - 1:
            new_matrix = self.after_move((i + 1, j), (i, j))
            if self.get_id(new_matrix) not in alreadys:
                new_matrixes.append(new_matrix)
        if j > 0:
            new_matrix = self.after_move((i, j - 1), (i, j))
            if self.get_id(new_matrix) not in alreadys:
                new_matrixes.append(new_matrix)
        if j < SIZE - 1:
            new_matrix = self.after_move((i, j + 1), (i, j))
            if self.get_id(new_matrix) not in alreadys:
                new_matrixes.append(new_matrix)
        return new_matrixes




