import streamlit as st

st.set_page_config(page_title="DFS Search Algorithm", page_icon="🌲")

st.title("🌲 Depth-First Search (DFS)")
st.subheader("AI Search Algorithm Demonstration")
st.write("This Streamlit app demonstrates how **Depth-First Search (DFS)** works on a directed graph "
         "based on the topic from Chapter 2: Search Algorithms.")

# Define the directed graph
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F', 'H'],
    'H': [],
    'F': []
}

st.subheader("Graph Structure")
st.json(graph)

# DFS Function
def dfs(graph, start, visited=None, level=0, levels=None):
    if visited is None:
        visited = []
        levels = {start: 0}
    visited.append(start)
    for neighbour in sorted(graph[start]):
        if neighbour not in visited:
            levels[neighbour] = level + 1
            dfs(graph, neighbour, visited, level + 1, levels)
    return visited, levels

# Input Section
start_node = st.text_input("Enter the starting node (default = A):", "A").upper()

if st.button("Run DFS"):
    if start_node in graph:
        result, levels = dfs(graph, start_node)
        st.success(f"Traversal Order: {' → '.join(result)}")
        st.write("### Level Explanation:")
        for node in result:
            st.write(f"**Level {levels[node]}:** {node}")
        st.info("DFS explores as deep as possible before backtracking using recursion (stack).")
    else:
        st.error("Invalid node. Please enter a valid node label (A–H).")

st.markdown("---")
st.caption("Developed for BSD3513 – Introduction to Artificial Intelligence | UMPSA 2025")
