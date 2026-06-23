import heapq

def k_duong_di_ngan_nhat(k=3):
    G1 = {
        0: [(1, 6), (2, 1)],  
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    s, t = 0, 4
    
    count = {v: 0 for v in G1}  # Theo dõi số lần đỉnh được xử lý 
    pq = [(0, s)]
    results = []
    
    while pq and count[t] < k:
        d, u = heapq.heappop(pq)
        count[u] += 1
        
        if u == t:
            results.append(d)
            
        if count[u] < k:  # Đã sửa dấu từ <= thành <
            for v, weight in G1[u]:
                heapq.heappush(pq, (d + weight, v))
                
    return results

print(k_duong_di_ngan_nhat(3))