import heapq

def duong_di_xac_suat_lon_nhat():
    # Đồ thị mẫu với trọng số là xác suất [0, 1] 
    graph = {
        0: [(1, 0.4), (2, 0.8)],
        1: [(3, 0.5)],
        2: [(1, 0.9), (3, 0.2)],
        3: []
    }
    s, t = 0, 3
    
    probs = {v: 0.0 for v in graph}
    probs[s] = 1.0
    pq = [(-1.0, s)]  # Đảo dấu sang âm để dùng Min-Heap mô phỏng Max-Heap [cite: 127]
    
    while pq:
        p, u = heapq.heappop(pq)
        p = -p  # Khôi phục giá trị dương ban đầu
        
        if p < probs[u]: continue
        if u == t: return p
        
        for v, edge_prob in graph[u]:
            # Phép toán relax nhân xác suất 
            if probs[u] * edge_prob > probs[v]:
                probs[v] = probs[u] * edge_prob
                heapq.heappush(pq, (-probs[v], v))
    return probs[t]

print(f"Xác suất thành công lớn nhất: {duong_di_xac_suat_lon_nhat()}")