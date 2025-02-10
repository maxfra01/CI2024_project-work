import numpy as np
from node import Node, UNARY_OPERATORS, BINARY_OPERATORS

class Tree:
    def __init__(self, num_variables, max_depth, root=None):
        self.max_depth = max_depth
        self.num_variables = num_variables
        
        if root is None:
            self.root = self.grow(max_depth)
        else:
            self.root = root
        
    def __str__(self):
        return str(self.root)
    
    def copy(self):
        return Tree(self.num_variables, self.max_depth, self.root.copy())
    
    def evaluate(self, x):
        return self.root.evaluate(x)
    
    def get_depth(self):
        return self.root.depth()
    
    def grow(self, max_depth):
        self.max_depth = max_depth
        self.root = self._grow(max_depth)
        return self.root
    
    def _grow(self, max_depth, current_depth=0):
        if current_depth == max_depth:
            if np.random.rand() < 0.6:
                return Node(f"x[{np.random.randint(0, self.num_variables)}]")
            else:
                return Node(np.random.uniform(-5, 5))
        else:
            if np.random.rand() < 0.6:
                return Node(np.random.choice(BINARY_OPERATORS), self._grow(max_depth, current_depth+1), self._grow(max_depth, current_depth+1))
            else:
                return Node(np.random.choice(UNARY_OPERATORS), self._grow(max_depth, current_depth+1))
        
