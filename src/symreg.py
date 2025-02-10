import numpy as np
from tqdm import tqdm
from tree import Tree
from genetic_stuff import recombination_xover, fitness, mse, tournament_selection, subtree_mutation, mutation_point, mutation_hoist, mutation_permutation, tune_constants
import warnings
import pickle
warnings.filterwarnings("ignore")


    

def symreg(problem_number):
    
    # Get the problem data
    problem = np.load(f'data/problem_{problem_number}.npz')
    X = problem['x']
    Y = problem['y']

    # Set the parameters
    VARIABLES = X.shape[0]
    FOREST_SIZE = 100
    OFFSPRING_SIZE = int(FOREST_SIZE * 0.05)
    TOURNAMENT_SIZE = int(FOREST_SIZE * 0.1)
    GENERATIONS = 300
    PM = 0.1
    RESUME = 0
    
    print(f"Problem {problem_number}, Variables: {VARIABLES}, Forest size: {FOREST_SIZE}, Offspring size: {OFFSPRING_SIZE}, Tournament size: {TOURNAMENT_SIZE}, Generations: {GENERATIONS}, PM: {PM}")

           
    # Generate the random forest
    forest = [Tree(max_depth=max(2, VARIABLES) , num_variables=VARIABLES) for _ in range(FOREST_SIZE)]
    champion = None
    
    # Resume from checkpoint
    if RESUME:
        with open(f"checkpoints/champion_problem{problem_number}.pkl", "rb") as f:
            champion = pickle.load(f)
            forest[0] = champion
            print(f"Resuming from checkpoint, champion: {champion}") 

    # Set the genetic operators
    xover = recombination_xover
    mutation_operators = [mutation_hoist, mutation_point, mutation_permutation]

    # Run the genetic algorithmc
    for g in tqdm(range(GENERATIONS)):
        
        o = []
        for _ in range(OFFSPRING_SIZE):
            
            mutation = np.random.choice(mutation_operators)
            
            # Select the parents
            parent1 = tournament_selection(forest, X, Y, TOURNAMENT_SIZE)
            parent2 = tournament_selection(forest, X, Y, TOURNAMENT_SIZE)
            
            # Apply the genetic operators
            if np.random.rand() < PM:
                o.append(mutation(parent1))
                o.append(mutation(parent2))
            o.extend(xover(parent1, parent2))
            

        # Add some mutations to the champion
        if champion is not None:
            o.append(mutation(champion))
            o.extend(xover(parent1, champion))
            o.extend(xover(parent2, champion))   
        
        # Add the offspring to the population
        forest.extend(o)
        forest = sorted(forest, key=lambda tree: fitness(tree, X, Y), reverse=True)
        champion = forest[0]
        
        # Check for extinction event if the champion is too dominant
        champion_count = len([tree for tree in forest if str(tree) == str(forest[0])])
        if champion_count > FOREST_SIZE * 0.05:
            print("Extinction event")
            new_population = []
            for _ in range(FOREST_SIZE - 1):
                new_population.append(Tree(max_depth=max(2,VARIABLES) , num_variables=VARIABLES))
            forest = [forest[0]] + new_population
            #print(len(forest))
        
        # Ensuring same population size
        forest = forest[:FOREST_SIZE]
        
        # Print the generation results
        print(f"Generation {g}:")
        print(f"\tMSE: {mse(champion, X, Y)}")
        print(f"\tChampion: {champion}")
        
        # Save champion to extend experiments
        if g +1 == GENERATIONS:
            with open(f"checkpoints/champion_problem{problem_number}.pkl", "wb") as f:
                pickle.dump(champion, f)
        
    print("Final results:")
    print(f"Final champion: {champion}")
    print(f"MSE: {mse(champion, X, Y)}")
    
    print("Tuning the constants...")
    # Tune the constants
    #champion = tune_constants(champion, X, Y)
    
    print("Final results after tuning:")
    print(f"Final champion: {champion}")
    print(f"MSE: {mse(champion, X, Y)}")
    
    with open(f'outputs/problem_{problem_number}.txt', 'a') as f:
        f.write(f"Problem: {problem_number}\n")
        f.write(f"Champion: {champion}\n")
        f.write(f"MSE: {mse(champion, X, Y)}\n")

for p in [4]:
    symreg(problem_number=p)
