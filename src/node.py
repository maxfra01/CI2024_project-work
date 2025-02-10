import numpy as np

UNARY_OPERATORS = ['sin', 'cos', 'exp', 'log']
BINARY_OPERATORS = ['add', 'subtract', 'multiply', 'divide', 'power']

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
        
    def is_binary_op(self):
        return self.value in BINARY_OPERATORS 
    
    def is_unary_op(self):
        return self.value in UNARY_OPERATORS
    
    def is_terminal(self):
        return not self.is_binary_op() and not self.is_unary_op()
    
    def is_constant(self):
        return self.is_terminal() and not 'x' in str(self.value)
    
    def evaluate(self, x):
        try:
            if self.is_binary_op():
                left_val = self.left.evaluate(x)
                right_val = self.right.evaluate(x)
                
                if self.value == 'add':
                    result =  left_val + right_val
                elif self.value == 'subtract':
                    result = left_val - right_val
                elif self.value == 'multiply':
                    if abs(left_val) < 1e50 and abs(right_val) < 1e50:
                        result = left_val * right_val
                    else:
                        result = float('inf')
                
                elif self.value == 'power':
                    if left_val < 0 and right_val < 1:
                        result = 1e10
                    else:
                        result = left_val ** right_val
                elif self.value == 'divide':
                    if abs(right_val) < 1e-20:
                        result = 1e10
                    elif abs(left_val) > 1e50 and abs(right_val) > 1e5:
                        result = 1e10
                    else:
                        result = left_val / right_val
                
                else:
                    raise ValueError(f"Unknown operator {self.value}")
                
            elif self.is_unary_op():
                arg = self.left.evaluate(x)
                
                if self.value == 'sin':
                    result = np.sin(arg)
                elif self.value == 'cos':
                    result = np.cos(arg)
                elif self.value == 'exp':
                    result = np.exp(arg)
                elif self.value == 'log':
                    if arg < 0:
                        result = 1e10
                    else:
                        result = np.log(arg)
                else:
                    raise ValueError(f"Unknown operator {self.value}")
                            
            elif self.is_terminal():
                if 'x' in self.value:
                    result = x[int(self.value[2:-1])]
                else:
                    result = float(self.value)
                              
        except OverflowError:
            result = float('inf')
        except Exception as e:
            result = 1e10             
        
        return result

    def __str__(self):
        if self.is_binary_op():
            if self.value == 'add' :
                return f"({self.left} + {self.right})"
            elif self.value == 'subtract':
                return f"({self.left} - {self.right})"
            elif self.value == 'multiply':
                return f"({self.left} * {self.right})"
            elif self.value == 'power':
                return f"({self.left} ** {self.right})"
            elif self.value == 'divide':
                return f"({self.left} / {self.right})"
        elif self.is_unary_op():
            return f"{self.value}({self.left})"
        else:
            return str(self.value)
        
    def depth(self):
        if self.is_terminal():
            return 1
        elif self.is_binary_op():
            return 1 + max(self.left.depth(), self.right.depth())
        elif self.is_unary_op():
            return 1 + self.left.depth()
        
        
    def copy(self):
        if self.is_terminal():
            return Node(self.value)
        elif self.is_binary_op(): 
            return Node(self.value, self.left.copy(), self.right.copy())
        elif self.is_unary_op():
            return Node(self.value, self.left.copy())
        
               
    def get_all_nodes(self):
        nodes = [self]
        if self.is_binary_op():
            nodes.extend(self.left.get_all_nodes())
            nodes.extend(self.right.get_all_nodes())
        elif self.is_unary_op():
            nodes.extend(self.left.get_all_nodes())
        return nodes
    
    def replace_child(self, old_child, new_child):
        if self.left == old_child:
            self.left = new_child
        elif self.right == old_child:
            self.right = new_child
        else:
            raise ValueError("Old child not found")