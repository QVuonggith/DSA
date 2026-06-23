def bellman_ford():
    # Đồ thị có cạnh âm (2 -> 1 với trọng số -4) 
    graph = {
        0: [(1, 2), (2, 5)],
        1: [],
        2: [(1, -4)]
    }
    num_vertices = 3
    s = 0
    
    dist = [float('inf')] * num_vertices
    dist[s] = 0
    
    # Vòng lặp nới lỏng n - 1 lần
    for _ in range(num_vertices - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    return dist

print(bellman_ford())