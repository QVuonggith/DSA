import heapq
import time
import random

# =====================================================================
# 1. PHIÊN BẢN DIJKSTRA GỐC: O(V^2) - Duyệt mảng (Thích hợp đồ thị dày)
# =====================================================================
def dijkstra_v2(graph, num_vertices, s):
    dist = [float('inf')] * num_vertices
    visited = [False] * num_vertices
    dist[s] = 0
    
    for _ in range(num_vertices):
        # Chọn đỉnh u chưa chốt có dist[u] nhỏ nhất bằng cách duyệt qua V đỉnh
        u = -1
        min_d = float('inf')
        for v in range(num_vertices):
            if not visited[v] and dist[v] < min_d:
                min_d = dist[v]
                u = v
                
        if u == -1: 
            break
            
        visited[u] = True
        
        # Nới lỏng (Relaxation) các cạnh kề của u
        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                
    return dist

# =====================================================================
# 2. PHIÊN BẢN DIJKSTRA CẢI TIẾN: O(E log V) - Dùng Min-Heap
# =====================================================================
def dijkstra_heap(graph, num_vertices, s):
    dist = [float('inf')] * num_vertices
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]: 
            continue
            
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist

# =====================================================================
# 3. CHƯƠNG TRÌNH CHẠY THỬ NGHIỆM VÀ IN KẾT QUẢ THEO VÍ DỤ
# =====================================================================
# Cài đặt số lượng đỉnh lớn (ví dụ: 1000 đỉnh)
num_vertices = 1000
dense_graph = {i: [] for i in range(num_vertices)}

print("Đang tạo dữ liệu đồ thị dày (1000 đỉnh, ~500,000 cạnh)...")
# Sinh đồ thị dày: Mỗi đỉnh nối tới hầu hết các đỉnh khác với xác suất > 50%
for u in range(num_vertices):
    for v in range(num_vertices):
        if u != v and random.random() > 0.5:
            weight = random.randint(1, 20)
            dense_graph[u].append((v, weight))
            
print("\n--- BẮT ĐẦU ĐO THỜI GIAN CHẠY ---")

# Đo thời gian bản gốc O(V^2)
start_time = time.time()
res_v2 = dijkstra_v2(dense_graph, num_vertices, 0)
time_v2 = time.time() - start_time
print(f"1. Bản gốc O(V^2) duyệt mảng mất:   {time_v2:.5f} giây")

# Đo thời gian bản Heap O(E log V)
start_time = time.time()
res_heap = dijkstra_heap(dense_graph, num_vertices, 0)
time_heap = time.time() - start_time
print(f"2. Bản Heap O(E log V) mất:        {time_heap:.5f} giây")

# Kiểm tra tính đúng đắn của dữ liệu giữa 2 phiên bản
assert res_v2 == res_heap, "Lỗi: Kết quả khoảng cách của 2 thuật toán không khớp!"
print("\n=> Kết luận kết quả trùng khớp hoàn toàn.")

# In ra phân tích thực nghiệm dựa trên kết quả chạy được
if time_v2 < time_heap:
    print("=> Đúng như lý thuyết Bài 10: Trên đồ thị DÀY, bản O(V^2) chạy nhanh hơn vì bản Heap phải tốn quá nhiều chi phí push/pop liên tục vào hàng đợi ưu tiên.")
else:
    print("=> Bản Heap chạy nhanh hơn (do thư viện heapq của Python được tối ưu hóa bằng ngôn ngữ C rất mạnh).")