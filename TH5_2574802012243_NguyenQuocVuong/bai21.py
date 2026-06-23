import heapq

def dijkstra_trang_thai_mo_rong():
    # Đồ thị G1 mở rộng
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: []
    }
    # Giả định đỉnh 2 và 3 là các trạm nạp nhiên liệu
    fuel_stations = {2, 3}
    max_fuel = 5  # Dung tích bình chứa xăng tối đa
    
    s, t = 0, 5
    
    # dist[(u, f)] là chi phí nhỏ nhất để đến đỉnh u với lượng nhiên liệu còn lại là f
    dist = {}
    
    # Hàng đợi ưu tiên lưu: (chi_phí, đỉnh_hiện_tại, nhiên_liệu_còn_lại)
    pq = [(0, s, max_fuel)]
    dist[(s, max_fuel)] = 0
    
    while pq:
        d, u, f = heapq.heappop(pq)
        
        if d > dist.get((u, f), float('inf')):
            continue
            
        if u == t:
            return f"Chi phí nhỏ nhất: {d} (Nhiên liệu khi tới đích: {f})"
            
        for v, weight in graph[u]:
            # Di chuyển đến v tốn 1 đơn vị nhiên liệu (giả định mỗi chặng đi mất 1 đơn vị xăng)
            next_fuel = f - 1
            
            if next_fuel >= 0:
                # Nếu v là trạm nạp xăng, nạp đầy lại bình
                if v in fuel_stations:
                    next_fuel = max_fuel
                    
                if d + weight < dist.get((v, next_fuel), float('inf')):
                    dist[(v, next_fuel)] = d + weight
                    heapq.heappush(pq, (d + weight, v, next_fuel))
                    
    return "Không có đường đi hợp lệ với lượng nhiên liệu này"

print(dijkstra_trang_thai_mo_rong())