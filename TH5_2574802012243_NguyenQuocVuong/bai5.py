INF = float('inf')
 
adj = {
    0: [(1,5),(2,3)],        # A
    1: [(0,5),(2,1),(3,2)],  # B
    2: [(0,3),(1,1),(3,6)],  # C
    3: [(1,2),(2,6),(4,4)],  # D
    4: [(3,4)],              # E
}
 
def dijkstra(adj, n, s):
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n
 
    for _ in range(n):
        u = min((v for v in range(n) if not visited[v]), key=lambda v: dist[v])
        if dist[u] == INF:
            break
        visited[u] = True
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
 
    return dist
 
names = ['A','B','C','D','E']
dist = dijkstra(adj, 5, 0)
 
for i, d in enumerate(dist):
    print(f"dist[{names[i]}] = {d if d < INF else -1}")
