import heapq

def dijkstra_minimax():
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    s, t = 0, 5
    dist = {v: float('inf') for v in G1}
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, weight in G1[u]:
            # Phép relax minimax: lấy giá trị cực đại trên lộ trình hiện tại 
            current_bottleneck = max(dist[u], weight)
            if current_bottleneck < dist[v]:
                dist[v] = current_bottleneck
                heapq.heappush(pq, (dist[v], v))
    return dist[t]

print(dijkstra_minimax())