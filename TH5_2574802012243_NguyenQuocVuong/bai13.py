import heapq

def dem_so_duong_di_ngan_nhat():
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
    ways = {v: 0 for v in G1}  # Mảng lưu số lượng đường đi 
    dist[s] = 0
    ways[s] = 1
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, weight in G1[u]:
            # Trường hợp tìm thấy đường ngắn hơn
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                ways[v] = ways[u]
                heapq.heappush(pq, (dist[v], v))
            # Trường hợp tìm thấy một đường đi khác có cùng độ dài tối ưu [cite: 93]
            elif dist[u] + weight == dist[v]:
                ways[v] += ways[u]
                
    return ways

print(dem_so_duong_di_ngan_nhat())