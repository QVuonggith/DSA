import heapq

def duong_di_ngan_nhi():
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    s, t = 0, 5
    
    # Khởi tạo mảng lưu khoảng cách ngắn nhất (dist1) và ngắn nhì (dist2) [cite: 97]
    dist1 = {v: float('inf') for v in G1}
    dist2 = {v: float('inf') for v in G1}
    
    dist1[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist2[u]: continue
        
        for v, weight in G1[u]:
            total = d + weight
            if total < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = total
                heapq.heappush(pq, (dist1[v], v))
            elif dist1[v] < total < dist2[v]:
                dist2[v] = total
                heapq.heappush(pq, (dist2[v], v))
                
    return dist2[t]

print(duong_di_ngan_nhi())