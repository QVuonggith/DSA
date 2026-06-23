import heapq

def so_dinh_trong_ban_kinh(D=3):
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    
    s = 0
    dist = {v: float('inf') for v in G1}
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, weight in G1[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    # Đếm các đỉnh có khoảng cách ngắn nhất <= D [cite: 74]
    count = sum(1 for v in dist if dist[v] <= D)
    return count

print(f"{so_dinh_trong_ban_kinh(3)}")