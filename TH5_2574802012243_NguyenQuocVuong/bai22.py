import heapq

def gioi_han_canh_trung_chuyen(max_edges=2):
    G1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    s, t = 0, 4
    
    # dist[(u, e)] là chi phí nhỏ nhất tới u dùng đúng e cạnh
    dist = {}
    pq = [(0, s, 0)]  # (chi_phí, đỉnh, số_cạnh_đã_dùng)
    dist[(s, 0)] = 0
    
    val_min = float('inf')
    
    while pq:
        d, u, edges = heapq.heappop(pq)
        
        if d > dist.get((u, edges), float('inf')):
            continue
            
        if u == t:
            val_min = min(val_min, d)
            
        # Nếu chưa vượt quá giới hạn cạnh, cho phép loang tiếp
        if edges < max_edges:
            for v, weight in G1[u]:
                if d + weight < dist.get((v, edges + 1), float('inf')):
                    dist[(v, edges + 1)] = d + weight
                    heapq.heappush(pq, (d + weight, v, edges + 1))
                    
    return val_min if val_min != float('inf') else -1

# Ví dụ đi từ 0 đến 4 dùng tối đa k=2 cạnh (Đường 0 -> 2 -> 4 có độ dài 1 + 8 = 9)
k = 2
print(f": Chi phí nhỏ nhất từ 0 -> 4 dùng tối đa {k} cạnh là: {gioi_han_canh_trung_chuyen(k)}")