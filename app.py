import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from astar import a_star_search

st.title("A* Search Digit Puzzle Solver")
st.write("Enter a start, goal, and forbidden states to see the optimal path and search graph.")
st.markdown(
    """
    📖 [Read full project instructions on GitHub](https://github.com/hamdamme/astar_search#readme)
    """,
    unsafe_allow_html=True
)
# User input
start = st.text_input("Start state", "565")
goal = st.text_input("Goal state", "777")
bad_states = st.text_input("Bad states (comma separated)", "665,666,677")

if st.button("Run A* Search"):
    bad = set(int(x.strip()) for x in bad_states.split(",") if x.strip().isdigit())
    path, trace = a_star_search(start, goal, bad)

    if path:
        # Ensure everything is string for NetworkX consistency
        path = [str(p) for p in path]

        st.success("Optimal Path: " + " → ".join(path))

        # Show search trace
        st.subheader("Search Trace")
        for step in trace:
            st.text(step)

               # --- Visualization ---
        st.subheader("Search Graph")

        G = nx.DiGraph()
        edges = []

        # Parse trace to extract parent-child edges
        parent = None
        for line in trace:
            if line.startswith("Expanding Node:"):
                parent = str(line.split()[2])
            elif line.strip().startswith("Generated successor:") and parent:
                child = str(line.split()[2])
                edges.append((parent, child))

        # Build graph
        G.add_edges_from(edges)

        # Make sure all path nodes exist in the graph
        for node in path:
            G.add_node(node)

        # Highlight optimal path
        path_edges = list(zip(path, path[1:])) if path else []

        pos = nx.spring_layout(G, seed=42)  # consistent layout
        plt.figure(figsize=(8, 6))

        # Draw all nodes/edges
        nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", arrows=True)

        # Highlight path nodes + edges
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange")
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.error("No path found.")