# A* Search Algorithm – Digit Puzzle Solver

This project implements an A* search algorithm in Python to solve a 3-digit digit puzzle.  
The puzzle transforms a starting number into a goal number by incrementing or decrementing digits, while avoiding forbidden states.

## The Puzzle Rules
- You start with a **3-digit number** (S).  
- You want to reach a **goal number** (G).  
- You may also have a list of **forbidden numbers** (bad states) that you must avoid.  

### Allowed Moves
1. In one move, you can **increase or decrease a single digit by 1**.  
   - Example: `678 → 679` (increase last digit)  
   - Example: `234 → 134` (decrease middle digit)  
2. Digits must stay between **0 and 9** (no “carry” to other digits).  
3. You cannot move into a **bad state**.  
4. You cannot change the **same digit twice in a row**.  
5. Every move has a **cost of 1**.  

### Goal
Find the **shortest path** from `S` to `G` while respecting all rules.


## Heuristic (h)
The heuristic estimates the distance to the goal by comparing each digit:  

```
h(n) = |G1 - n1| + |G2 - n2| + |G3 - n3|
````

Example:  
- Current = `234`  
- Goal = `789`  
- h = |7−2| + |8−3| + |9−4| = 5 + 5 + 5 = **15**

This ensures A* finds the optimal path.

## Features
- Implements the A* search algorithm with cost + heuristic.  
- Expands nodes step by step and records the trace.  
- Detects forbidden states (`bad` numbers) and avoids them.  
- Reconstructs the **optimal path** from start to goal.  
- Supports **command-line usage** and **interactive Streamlit web app**.  

## Installation

Clone this repository:
```bash
git clone https://github.com/hamdamme/astar_search.git
cd astar_search
````

Install dependencies (for the web app):

```bash
pip install -r requirements.txt
```

## How to Run

### Command Line

```bash
python astar.py S=<start> G=<goal> "bad=[list of bad states]"
```

#### Example

```bash
python astar.py S=565 G=777 "bad=[665,666,677]"
```

Output:

```
Expanding Node: 565 with cost 0
  Generated successor: 566 from digit 2
  Generated successor: 564 from digit 2
  ...
Optimal Path: 565 -> 575 -> 675 -> 676 -> 776 -> 777
```

### Streamlit Web App

Run locally:

```bash
streamlit run app.py
```
## Project Structure

```
astar_search/
 ├── astar.py          # Core A* search implementation
 ├── app.py            # Streamlit interface with graph visualization
 ├── requirements.txt  # Dependencies
 └── README.md         # Project documentation
```