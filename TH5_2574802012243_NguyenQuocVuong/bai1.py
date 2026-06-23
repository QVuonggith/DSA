# Xây dựng adjacency list không cần defaultdict
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 3, 1),
    (2, 1, 2),
    (2, 3, 5),
    (2, 4, 8),
    (3, 4, 3),
    (3, 5, 6),
    (4, 5, 2),
]

adj = {i: [] for i in range(6)}  # khởi tạo 6 đỉnh

for u, v, w in edges:
    adj[u].append((v, w))

# In kết quả
for v in range(6):
    print(f"adj[{v}] = {adj[v]}")