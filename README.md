# A* Search Algorithm – Digit Puzzle Solver

This project implements an **A\* search algorithm** in Python to solve a digit-based puzzle.  
The puzzle transforms a starting number into a goal number by incrementing or decrementing digits, while avoiding forbidden states.

---

## ✨ Features
- Implements the A* search algorithm with cost + heuristic.
- Expands nodes step by step and prints progress.
- Detects forbidden states (`bad` numbers) and avoids them.
- Reconstructs the optimal path from start to goal.
- Simple command-line usage.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/hamdamme/astar_search.git
   cd astar_search

# Run the program
    python astar.py S=<start> G=<goal> "bad=[list of bad states]"

# Examples
   python astar.py S=565 G=777 "bad=[665,666,677]"
 # Output 
    Expanding Node: 565 with cost 0
  Generated successor: 566 from digit 2
  Generated successor: 564 from digit 2
  ...
Optimal Path: 565 -> 575 -> 675 -> 676 -> 776 -> 777
