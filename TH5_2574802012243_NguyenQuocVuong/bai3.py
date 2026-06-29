def dijkstra_v2(matrix, s):
    V = len(matrix)
    dist = [float('inf')] * V
    dist[s] = 0
    visited = [False] * V

    for _ in range(V):
        u = -1
        min_dist = float('inf')
        for v in range(V):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        
        if u == -1:
            break
            
        visited[u] = True

        for v in range(V):
            if matrix[u][v] != float('inf') and not visited[v]:
                if dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]

    return dist

INF = float('inf')

G1 = [
    [0,   4,   1,   INF, INF, INF], # Đỉnh 0
    [4,   0,   2,   1,   INF, INF], # Đỉnh 1
    [1,   2,   0,   3,   6,   INF], # Đỉnh 2
    [INF, 1,   3,   0,   3,   5],   # Đỉnh 3
    [INF, INF, 6,   3,   0,   2],   # Đỉnh 4
    [INF, INF, INF, 5,   2,   0]    # Đỉnh 5
]

source = 0
result = dijkstra_v2(G1, source)

print(result)