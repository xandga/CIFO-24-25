"""Problem definition

Description: The IntBin problem consists of finding the integer
with greatest number of 1's in its binary representation

Search space: Integers from 1 to 15.

Representation: Binary string representing the integer.

Fitness function: f(x)= Number of 1's in binary representation of x

Neighbors: Each binary representation of an integer x has as neighbors any other binary with a bit flipped.

Goal: Maximize f(x).
"""

import random
from copy import deepcopy

from library.solution import Solution

class IntBinSolution(Solution):
    """The IntBin Optimization problem aims at finding the integer number
    between 1 and 15 with the greatest number of 1's in its binary representation
    """
    def __init__(self, repr=None):
        # Check if valid repr was passed
        if repr:
            if not isinstance(repr, str):
                raise ValueError("Representation must be a string")
            if (not len(repr) == 4) or (not set(repr).issubset({'0', '1'})):
                raise ValueError("IntBin solutions must be represented as binary strings of integers from 1 to 15")

        super().__init__(repr=repr)

    # Override the superclass's methods
    def random_initial_representation(self):
        # Generate random integer between 1 and 15
        random_n = random.randint(1, 15)
        # Transform it into its binary string representation with 4 digits
        return str(format(random_n, '04b'))

    def fitness(self):
        return self.repr.count('1')

# Algorithm specific
class IntBinHillClimbingSolution(IntBinSolution):
    def get_neighbors(self):
        neighbors = []

        # Edge case: Number 1 ('0001') only has 3 neighbors
        if self.repr == "0001":
            neighbors_repr = ["1001", "0101", "0011"]
            for neighbor_repr in neighbors_repr:
                neighbors.append(IntBinHillClimbingSolution(repr=neighbor_repr))
        else:
            # Convert binary string to list of bits
            # Strings are not mutable, that's why we are converting to list
            repr_list = list(self.repr)
            for idx, digit in enumerate(repr_list):
                neighbor_list_repr = deepcopy(repr_list)
                
                if digit == '1':
                    neighbor_list_repr[idx] = '0'
                elif digit == '0':
                    neighbor_list_repr[idx] = '1'
                
                # Convert back to string
                neighbor_repr = "".join(neighbor_list_repr)
                # Create neighbor and add it to the list
                neighbors.append(IntBinHillClimbingSolution(repr=neighbor_repr))

        return neighbors
