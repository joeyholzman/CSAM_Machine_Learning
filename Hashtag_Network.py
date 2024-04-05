import networkx as nx

# Example co-occurrence matrix (replace this with your actual data)
co_occurrence_matrix = {
    'hashtag1': {'hashtag1': 10, 'hashtag2': 5, 'hashtag3': 2},
    'hashtag2': {'hashtag1': 5, 'hashtag2': 8, 'hashtag3': 3},
    'hashtag3': {'hashtag1': 2, 'hashtag2': 3, 'hashtag3': 6}
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes
for hashtag in co_occurrence_matrix:
    G.add_node(hashtag)

# Add edges
for source, targets in co_occurrence_matrix.items():
    for target, weight in targets.items():
        G.add_edge(source, target, weight=weight)

# Visualize the network
nx.draw(G, with_labels=True)

#This code creates a directed graph where nodes represent hashtags and edges represent co-occurrence relationships between hashtags.