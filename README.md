# A* Search Algorithm – Digit Puzzle Solver

This project implements the A* search algorithm to solve a 3-digit digit puzzle.  
The solver transforms a starting number into a goal number by incrementing or decrementing digits, while avoiding forbidden states.

---

## 🧩 Puzzle Rules

- You start with a **3-digit number** `S`.
- Your goal is to reach another **3-digit number** `G`.
- You may specify **forbidden states** (bad numbers) that must be avoided.

### Allowed Moves
1. **Increase or decrease one digit by 1**  
   - Example: `678 → 679` (increase)  
   - Example: `234 → 134` (decrease)
2. Digits stay between **0 and 9**
3. **Each move has a cost of 1**
4. The algorithm finds the **optimal (shortest) path**

---

## 🔍 Heuristic (h)

We use Manhattan distance over each digit:
```

h(n) = |G1 − n1| + |G2 − n2| + |G3 − n3|

````

Example: Current `234`, Goal `789` → `|7−2| + |8−3| + |9−4| = 15`

This admissible heuristic ensures A* finds the shortest path.

---

## 🚀 Features

- A* Search (cost + heuristic)
- Forbidden state avoidance
- Full expansion trace
- Optimal path reconstruction
- **Interactive Streamlit UI** with graph visualization

---

## 📦 Installation

```bash
git clone https://github.com/hamdamme/astar_search.git
cd astar_search
pip install -r requirements.txt
````

---

## 🖥️ Run via Command Line

```bash
python astar.py S=565 G=777 "bad=[665,666,677]"
```

**Example Output:**

```
Expanding Node: 565 with cost 0
  Generated successor: 566
  ...
Optimal Path: 565 -> 575 -> 675 -> 676 -> 776 -> 777
```

---

## 🌐 Run Streamlit Web App (Local)

```bash
streamlit run app.py
```

Open in browser: `http://localhost:8501`

---

## 🌍 Deployment to Render.com

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Optional: `render.yaml`

```yaml
services:
  - type: web
    name: astar-streamlit
    env: python
    plan: free
    autoDeploy: true
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 🗂️ Project Structure

```
astar_search/
 ├── astar.py          # Core A* algorithm
 ├── app.py            # Streamlit web app
 ├── requirements.txt  # Dependencies
 ├── render.yaml       # (Optional) Render deployment file
 └── README.md         # Project documentation
```