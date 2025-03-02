A modular optimization library designed to solve various optimization problems using optimization algorithms.

## How it works

The library follows a structured approach:

1. **Abstract Base Class (Solution)**
- Defines a generic solution structure for all optimization problems.
- Requires implementation of `fitness()` and `random_initial_value()`.
- Defined in `solution.py`

2. **Problem-Specific Solution Classes**

- Extend `Solution` and implement problem-specific methods.
- Implements the `fitness()` and `random_initial_value()` methods.
- Example: `TSPSolution` for the Traveling Salesperson Problem in `problems/tsp.py`

3. **Algorithm-Specific Solution Classes**
- Extend `Solution` and define a generic structure for each optimization algorithm.
- Requires implementation of methods specific to the optimization algorithm.
- Example: `HillClimbingSolution` in `algorithms/hill_climbing.py`

4. **Problem-Algorithm-Specific Solution Classes**
- Extend both a problem solution class and an optimization algorithm class.
- Implements the Algorithm-Specific abstract methods
- Example: `TSPHillClimbingSolution` inherits from `TSPSolution` and `HillClimbingSolution` available in `problems/tsp.py`.

Besides the Algorithm-Specific Solution Classes, implementations of the optimization algorithms are also available in the `algorithms` directory.

## Adding a New Optimization Problem

To solve a new optimization problem, create a new **problem-specific solution class** that extends `Solution` and that implements the specific `fitness()` and `random_initial_value()` methods for the optimization problem.


## Solving a New Optimization Problem using an Optimization Algorithm

Each problem can be optimized using different algorithms by defining a **problem-algorithm-specific solution class** that extends both the **problem-specific** solution class and the **algorithm-specific** solution class.

This class should implement the **algorithm-specific** abstract methods that are left to implement.

An initial solution to the optimization problem can be created using this class, and this inital solution can then be passed as argument to the optimization problem algorithm function.

