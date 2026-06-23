import heapq

def _mini_dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def duong_di_qua_dinh_bat_buoc():
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    s, t, k = 0, 5, 2  # Đỉnh k bắt buộc đi qua [cite: 91]
    
    dist_from_s = _mini_dijkstra(G1, s)
    dist_from_k = _mini_dijkstra(G1, k)
    
    # Kết quả dựa trên gợi ý dist(s,k) + dist(k,t) [cite: 90]
    return dist_from_s[k] + dist_from_k[t]

print(duong_di_qua_dinh_bat_buoc())