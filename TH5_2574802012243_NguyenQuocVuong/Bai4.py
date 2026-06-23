INF = float('inf')
 
adj = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5),(4,8)],
    3: [(4,3),(5,6)],
    4: [(5,2)],
    5: [],
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
 
dist = dijkstra(adj, 6, 0)
 
for i, d in enumerate(dist):
    print(f"dist[{i}] = {d if d < INF else -1}")
