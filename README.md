## Symbolic Regression in Pure Python

This is a simple implementation of symbolic regression in pure Python. It uses a genetic algorithm to evolve a population of expressions that best fit a given dataset. In each generation, the algorithm selects the best individuals with torunament selection, recombines them using crossover, and mutates (lower probability) them using mutation operations. The algorithm stops when the maximum number of generations is reached. An extinction mechanism is used to promote diversity in case the population converges to a local minimum. 

### Usage

The `symreg.py` script can be used to run the symbolic regression algorithm. It is sufficient to call the function `symreg` with the following parameters:
- `problem_number`: the number of the problem to solve (1,2,...,8).

### Classes
The main class is the `Node` class, which represents a node in the expression tree. The `Node` class has the following attributes:
- `value`: the value of the node
- `left`: the left child of the node
- `right`: the right child of the node
- `parent`: the parent of the node

The `Tree` class represents the expression tree and has the following attributes:
- `root`: the root node of the tree
- : `max_depth`: the maximum depth of the tree
- `num_variables`: the number of variables in the expression

### Functions

The genetic algorithm uses the following operations:
- `tournament_selection` : Selects the best individuals from the population using tournament selection method.
- `recombination_xover`: Recombines two individuals using crossover operation.
- `mutation_point`: Mutates an individual by changing a random node in the tree.
- `mutation_hoist`: Mutates an individual by changing a subtree in the tree.
- `mutation_permutation`: Mutates an individual by permuting the nodes in the tree.
- `fitness`: Evaluates the fitness of an individual by calculating the mean squared error between the individual's expression and the target dataset. It sets the mse value to infinty if the individual's expression has higher depth than the maximum depth allowed.

