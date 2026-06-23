import heapq

def trong_so_tren_dinh():
    # Đồ thị cơ sở ban đầu (chỉ chứa liên kết cạnh thô)
    base_graph = { 0: [1, 2], 1: [3], 2: [3], 3: [] }
    # Chi phí khi đi qua mỗi đỉnh [cite: 107]
    node_weights = {0: 1, 1: 4, 2: 2, 3: 5}
    
    # Xây dựng đồ thị liên kết mở rộng 
    extended_graph = {}
    for u in base_graph:
        extended_graph[f"{u}_in"] = [(f"{u}_out", node_weights[u])]
        extended_graph[f"{u}_out"] = []
        for v in base_graph[u]:
            extended_graph[f"{u}_out"].append((f"{v}_in", 0))
            
    # Tiến hành chạy thuật toán Dijkstra tiêu chuẩn trên đồ thị ảo mới
    s_node, t_node = "0_in", "3_out"
    dist = {v: float('inf') for v in extended_graph}
    dist[s_node] = 0
    pq = [(0, s_node)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, weight in extended_graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist[t_node]

print(f"Tổng chi phí qua đỉnh: {trong_so_tren_dinh()}")