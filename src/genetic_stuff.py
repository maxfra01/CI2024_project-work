import numpy as np
from tree import Tree
from tqdm import tqdm
from node import Node, UNARY_OPERATORS, BINARY_OPERATORS

def mse(tree: Tree, X: np.ndarray, Y: np.ndarray) -> float:
    X = X.T 
    Y = Y.T
    mse = 0
    for x, y in zip(X, Y):
        mse += (y - tree.evaluate(x))**2
    if np.isnan(mse):
        return float('inf')
    return mse / len(X)


def fitness(tree: Tree, X: np.ndarray, Y: np.ndarray) -> float:
    if tree.get_depth() > 16:
        mse_value = np.inf
    else:
        mse_value = mse(tree, X, Y)
    return - mse_value

def tournament_selection(forest: list[Tree], X: np.ndarray, Y: np.ndarray, tournament_size: int) -> Tree:
    tournament = list(np.random.choice(forest, tournament_size))
    tournament = sorted(tournament, key=lambda tree: fitness(tree, X, Y), reverse=True)
    return tournament[0]

def recombination_xover(t1, t2):
    t1 = t1.copy()
    t2 = t2.copy()
    
    t1_node = t1.root.get_all_nodes()
    t2_node = t2.root.get_all_nodes()
    
    t1_node = np.random.choice(t1_node)
    t2_node = np.random.choice(t2_node)
    
    t1_node.value, t2_node.value = t2_node.value, t1_node.value
    t1_node.left, t2_node.left = t2_node.left, t1_node.left
    t1_node.right, t2_node.right = t2_node.right, t1_node.right
    return t1, t2

def mutation_point(tree):
    tree = tree.copy()
    nodes = tree.root.get_all_nodes()
    node = np.random.choice(nodes)
    
    if node.is_binary_op():
        node.value = np.random.choice(BINARY_OPERATORS)
    elif node.is_unary_op():
        node.value = np.random.choice(UNARY_OPERATORS)
    else:
        if np.random.rand() < 0.5:
            node.value = f"x[{np.random.randint(0, tree.num_variables)}]"
        else:
            node.value = np.random.uniform(-5, 5)
    return tree

def mutation_hoist(tree):
    tree = tree.copy()
    nodes = tree.root.get_all_nodes()
    node = np.random.choice(nodes)
    
    tree.root = node
    return tree

def mutation_permutation(tree):
    tree = tree.copy()
    nodes = tree.root.get_all_nodes()
    node = np.random.choice(nodes)
    
    if node.is_binary_op():
        node.left, node.right = node.right, node.left
    
    return tree        
    
        
def tune_constants(tree, X, Y):
    all_nodes = tree.root.get_all_nodes()
    best_tree = tree.copy()
    best_mse = mse(tree, X, Y)
    
    for _ in tqdm(range(10000)):
        tree = best_tree.copy()
        for node in all_nodes:
            if not node.is_constant():
                continue
            node.value = np.random.uniform(-5, 5)
        
        new_mse = mse(tree, X, Y)
        if new_mse < best_mse:
            best_mse = new_mse
            best_tree = tree.copy()
        
                
    return best_tree
