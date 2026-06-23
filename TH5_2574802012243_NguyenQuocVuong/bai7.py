import heapq

def truy_vet_duong_di():
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    
    s, t = 0, 4
    dist = {v: float('inf') for v in G1}
    parent = {v: None for v in G1}
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        if u == t: break
            
        for v, weight in G1[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u  # Lưu vết đỉnh đi trước 
                heapq.heappush(pq, (dist[v], v))
                
    # Truy vết ngược từ đích t về s 
    path = []
    curr = t
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    return path

print(f"Đường đi chi tiết từ 0 đến 4: {truy_vet_duong_di()}")