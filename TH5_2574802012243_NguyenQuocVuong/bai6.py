import heapq

def dijkstra_s_to_t():
    # Khởi tạo đồ thị G1 dưới dạng danh sách kề độc lập [cite: 21, 22]
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
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        # Dừng sớm khi lấy được t ra khỏi hàng đợi 
        if u == t:
            break
            
        for v, weight in G1[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist[t]

print(f"Độ dài ngắn nhất từ 0 đến 4: {dijkstra_s_to_t()}")