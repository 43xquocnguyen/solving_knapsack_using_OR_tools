# Import Libraries
from ortools.algorithms import pywrapknapsack_solver
from read import *
import time

test_cases = read_test_cases()

# Declare the "solver" for the Knapsack Problem
solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 
    'Knapsack'
    )

# Solve the Test Case => Return the Object have the Results
def solve(test_case, limited_time):
    print("Test Case", test_case['path'].replace("\n", ""), "is being solved....")

    # Convert Test Case into Parameters
    values = [int(i) for i in test_case['values']]
    weights = [[int(i) for i in test_case['weights']]]
    capacity = [test_case['capacity']]

    # Solving
    solver.Init(values, weights, capacity)
    solver.set_time_limit(limited_time)

    # Result to Return
    result = {}

    time_start = time.time()
    result['total_value'] = solver.Solve()
    time_end = time.time()
    result['total_weight'] = 0
    result['packed_items'] = []
    result['packed_weights'] = []
    result['time'] = str(time_end - time_start) + "s"

    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            result['packed_items'].append(i)
            result['packed_weights'].append(weights[0][i])
            result['total_weight'] += weights[0][i]

    print("Test Case", test_case['path'].replace("\n", ""), "is solved in", result['time'] + "\n")
    return result

# Display the Result Object
def show(result):
    print("Total Value: " + str(result['total_value']))
    print("Total Weight: " + str(result['total_weight']))
    print("Packed Items:", result['packed_items'])
    print("Packed Weights:", result['packed_weights'])
    print("Time to Found:", result['time'])