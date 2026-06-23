import heapq

# 1. Hàm Dijkstra từ một nguồn cố định trả về mảng khoảng cách tới mọi đỉnh
def dijkstra_single_source(graph, s):
    dist = {v: float('inf') for v in graph}
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: 
            continue
        for v, weight in graph.get(u, []):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

# 2. Hàm Tiền xử lý (Precompute) chạy Dijkstra cho tất cả các đỉnh trong đồ thị
def precompute_all_pairs(graph):
    # Tạo ma trận bảng tra cứu khoảng cách: matrix_dist[s][t]
    matrix_dist = {}
    for vertex in graph:
        matrix_dist[vertex] = dijkstra_single_source(graph, vertex)
    return matrix_dist

# --- CHƯƠNG TRÌNH CHẠY THỬ NGHIỆM CHIẾN LƯỢC BÀI 23 ---

G1 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

print("--- BƯỚC 1: TIỀN XỬ LÝ ĐỒ THỊ (PRECOMPUTE) ---")
# Chạy Dijkstra từ mọi đỉnh để xây dựng trước cơ sở dữ liệu khoảng cách
bang_tra_cuu = precompute_all_pairs(G1)
print("Đã xây dựng xong bảng khoảng cách toàn bộ các cặp đỉnh.\n")

print("--- BƯỚC 2: XỬ LÝ CÁC TRUY VẤN ĐỒNG THỜI O(1) ---")
# Giả sử hệ thống nhận vào danh sách Q = 3 câu hỏi truy vấn cặp (s, t) khác nhau
queries = [
    (0, 4),  # Hỏi khoảng cách từ 0 đến 4
    (2, 5),  # Hỏi khoảng cách từ 2 đến 5
    (1, 4)   # Hỏi khoảng cách từ 1 đến 4
]

for idx, (s, t) in enumerate(queries, 1):
    # Tra cứu trực tiếp từ bảng đã tính trước mà không cần chạy lại Dijkstra
    khoang_cach = bang_tra_cuu[s][t]
    print(f"Truy vấn {idx}: Khoảng cách ngắn nhất từ {s} đến {t} là: {khoang_cach}")