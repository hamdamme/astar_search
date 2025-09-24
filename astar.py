# -*- coding: utf-8 -*-
"""
A* Search Algorithm Digit Puzzle Solver

Author: Hamdam Aynazarov
GitHub: https://github.com/hamdamme

Description:
    This program implements an A* search algorithm to solve a digit puzzle.
    It transforms a starting number into a goal number by incrementing or 
    decrementing digits while avoiding forbidden states.

Usage:
    python astar.py S=<start> G=<goal> "bad=[list of bad states]"

Example:
    python astar.py S=565 G=777 "bad=[665,666,677]"
"""

import sys

class Astar:
    def __init__(this, start, goal, predecessor=None, move_cost=0, transformed=None):
        this.start = start
        this.predecessor = predecessor
        this.transformed = transformed if transformed is not None else -1
        this.move_cost = this.count_move_cost(predecessor, move_cost)
        this.cost = this.move_cost + get_heuristic(this.start, goal)
     
    def count_move_cost(this, predecessor, start_cost):
        if predecessor is None:
            return start_cost
        else:
            return predecessor.move_cost + 1

    def generate_successors(this, goal, bad):
        successors = []
        start_str = str(this.start)
        for i, digit in enumerate(start_str):
            if i == this.transformed:
                continue
            current_digit = int(digit)
            if current_digit < 9:
                new_start = int(start_str[:i] + str(current_digit + 1) + start_str[i + 1:])
                if new_start not in bad:
                    successors.append(Astar(new_start, goal, this, transformed=i))
            if current_digit > 0:
                new_start = int(start_str[:i] + str(current_digit - 1) + start_str[i + 1:])
                if new_start not in bad:
                    successors.append(Astar(new_start, goal, this, transformed=i))
        
        return successors

def get_heuristic(start:str, goal:str)->int:
    start = str(start).zfill(3)
    goal = str(goal).zfill(3)
    differences = []
    for i in range(3):
        difference = abs(int(start[i]) - int(goal[i]))
        differences.append(difference)
    total_difference = sum(differences)
    return total_difference

def a_star_search(start, goal, bad):
    frontier = []
    start_node = Astar(int(start), int(goal))
    add_to_frontier(start_node, frontier)
    explored_set = set()
    trace = []
    while frontier:
        current_node = get_next_node(frontier)
        
        print(f"Expanding Node: {current_node.start} with cost {current_node.move_cost}")

        if current_node.start == int(goal):
            return reconstruct_path(current_node)

        explored_set.add(current_node.start)

        successors = current_node.generate_successors(int(goal), bad)
        for successor in successors:
            print(f"  Generated successor: {successor.start} from digit {successor.transformed}")
            if successor.start not in explored_set and all(successor.start != existing.start for existing in frontier):
                add_to_frontier(successor, frontier)
                

    return None, trace

def add_to_frontier(node, frontier):
    frontier.append(node)
    frontier.sort(key=lambda x: x.cost)
    
def get_next_node(frontier):
    return frontier.pop(0)

def reconstruct_path(node):
    path = []
    while node:
        path.append(str(node.start))
        node = node.predecessor
    path.reverse()
    return path

def parse_args():
    if len(sys.argv) < 2:
        print("Usage: python astar.py help")
        return

    if sys.argv[1] == 'help':
        print("Hint:    python script.py S=<S> G=<G> \"bad=[bad1,bad2,...]\"")
        print("Example: python script.py S=565 G=777 \"bad=[665,666,677]\"")
        print("Expected output:  Optimal Path is 565 -> 575 -> 675 -> 676 -> 776 -> 777")
        return

    S = G = None
    bad_numbers = set()

    for arg in sys.argv[1:]:
        if arg.startswith("S="):
            S = arg.split("=")[1]
        elif arg.startswith("G="):
            G = arg.split("=")[1]
        elif arg.startswith("bad="):
            bad_numbers = set([int(x) for x in arg[4:].strip('[]').split(',')])

    if S and G:
        path = a_star_search(S, G, bad_numbers)
        if path:
            print("Optimal Path:", ' -> '.join(path))
        else:
            print("No path found.")
    else:
        print("Invalid arguments. Type 'python astar.py help' for usage information.")

if __name__ == "__main__":
    parse_args()