import heapq

def dijkstra_heap(graph, s):
    # Khởi tạo cấu trúc dữ liệu tổng quát cho bài toán đồ thị thưa 
    dist = {v: float('inf') for v in graph}
    dist[s] = 0
    pq = [(0, s)]  # Min-heap lưu cặp (khoảng_cách, đỉnh) 
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, weight in graph.get(u, []):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist