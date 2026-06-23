import heapq

def multi_source_dijkstra():
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    
    sources = [0, 3]  # Tập nguồn ban đầu 
    dist = {v: float('inf') for v in G1}
    pq = []
    
    # Kỹ thuật siêu nguồn: Khởi tạo tất cả các nguồn vào Heap với dist = 0 
    for src in sources:
        dist[src] = 0
        heapq.heappush(pq, (0, src))
        
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, weight in G1[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

print(multi_source_dijkstra())