import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.DiGraph()

# Thêm các nút (khái niệm)
nodes = ["α", "β", "δ", "a", "b", "c", "ρ", "h", "S"]
G.add_nodes_from(nodes)

# Thêm các mối quan hệ (cung)
edges = [
    ("α", "a"), ("β", "b"), ("δ", "c"), # Góc liên quan đến cạnh
    ("a", "ρ"), ("b", "ρ"), ("c", "ρ"), # Cạnh liên quan đến nửa chu vi
    ("ρ", "S"), ("a", "S"), ("b", "S"), ("c", "S"), # Công thức Heron
    ("h", "S"), ("c", "S") # Công thức chiều cao
]

G.add_edges_from(edges)

# Vẽ đồ thị
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, font_weight='bold', arrows=True)
plt.show()
