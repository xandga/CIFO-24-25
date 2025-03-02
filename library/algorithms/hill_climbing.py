from copy import deepcopy
from abc import ABC, abstractmethod
from library.solution import Solution

class HillClimbingSolution(Solution, ABC):
    @abstractmethod
    def get_neighbors(self):
        pass


def hill_climbing(initial_solution: HillClimbingSolution, maximization=False, max_iter=99999, verbose=False):
    current = initial_solution
    improved = True
    iter = 1

    while improved:
        if verbose:
            print(f'Current solution: {current} with fitness {current.fitness()}')

        improved = False
        neighbors = current.get_neighbors()

        for neighbor in neighbors:

            if verbose:
                print('Neighbor:', neighbor)

            if maximization and (neighbor.fitness() >= current.fitness()):
                current = deepcopy(neighbor)
                improved = True
            elif not maximization and (neighbor.fitness() <= current.fitness()):
                current = deepcopy(neighbor)
                improved = True
        
        iter += 1
        if iter == max_iter:
            break
    
    return current