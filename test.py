from Domains.BlockWorld import BlockDomain
from Problems.Problem import Problem
from Planners.ForwardPlanner import ForwardPlanner
from Planners.BackwardPlanner import BackwardPlanner
from Model.Predicate import Predicate
from Model.State import State

def main():
    # Create a BlockDomain with 3 blocks
    domain = BlockDomain(3)

    # Get the entities from the domain
    block1 = domain.entities[0]
    block2 = domain.entities[1]
    block3 = domain.entities[2]
    table = domain.entities[3]

    # Create the initial state
    initial_state = State("init", [
        Predicate("On", [block1, table]),
        Predicate("On", [block2, block1]),
        Predicate("On", [block3, block2]),
        Predicate("Clear", [block3])
    ])

    # Create the goal state
    goal_state = State("goal", [
        Predicate("On", [block1, block2]),
        Predicate("On", [block2, block3]),
        Predicate("On", [block3, table])
    ])

    # Create the problem
    problem = Problem(domain)
    problem.initial_state = initial_state
    problem.goal_state = goal_state

    # Create the planners
    forward_planner = ForwardPlanner(problem)
    backward_planner = BackwardPlanner(problem)

    # Solve the problem with the forward planner
    forward_solution = forward_planner.search()

    # Solve the problem with the backward planner
    backward_solution = backward_planner.search()

    # Print the solutions
    print("Forward Planner Solution:")
    for action in forward_solution:
        print(action)

    print("\nBackward Planner Solution:")
    for action in backward_solution:
        print(action)

if __name__ == "__main__":
    main()