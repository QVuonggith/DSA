import heapq

def dijkstra_tren_luoi():
    # Lưới chi phí 3x3 theo dữ liệu đề bài [cite: 102, 103]
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]  # (chi_phí, dòng, cột) [cite: 101]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]: continue
        if r == rows - 1 and c == cols - 1:
            return d
            
        # Di chuyển 4 hướng [cite: 101]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

print(dijkstra_tren_luoi())