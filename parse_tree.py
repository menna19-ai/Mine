import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edge("¬", "∧1")

G.add_edge("∧1", "∧2")
G.add_edge("∧1", "→2")

G.add_edge("∧2", "¬2")
G.add_edge("∧2", "→1")

G.add_edge("¬2", "q1")

G.add_edge("→1", "p")
G.add_edge("→1", "r1")

G.add_edge("→2", "r2")
G.add_edge("→2", "q2")

pos = {
    "¬": (0, 4),

    "∧1": (0, 3),

    "∧2": (-1.5, 2),
    "→2": (1.5, 2),

    "¬2": (-2, 1),
    "→1": (-1, 1),

    "r2": (1, 1),
    "q2": (2, 1),

    "q1": (-2, 0),
    "p": (-1, 0),
    "r1": (0, 0)
}

labels = {
    "¬": "¬",
    "∧1": "∧",
    "∧2": "∧",
    "→2": "→",
    "¬2": "¬",
    "→1": "→",

    "q1": "q",
    "q2": "q",

    "r1": "r",
    "r2": "r",

    "p": "p"
}

nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=14
)

plt.title("Parse Tree")
plt.show()