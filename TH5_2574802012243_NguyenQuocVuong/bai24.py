import heapq

def heuristic(a, b):
    # Sử dụng hàm khoảng cách Manhattan làm Heuristic admissible [cite: 148]
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bai_24_a_star_grid():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start, goal = (0, 0), (2, 2)
    rows, cols = len(grid), len(grid[0])
    
    g_score = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    g_score[start] = grid[start[0]][start[1]]
    
    # Độ ưu tiên sắp xếp heap bằng f_score = g_score + h_score 
    pq = [(g_score[start] + heuristic(start, goal), start[0], start[1])]
    
    visited_count = 0
    while pq:
        f, r, c = heapq.heappop(pq)
        visited_count += 1
        
        if (r, c) == goal:
            return g_score[goal], visited_count
            
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                tentative_g = g_score[(r, c)] + grid[nr][nc]
                if tentative_g < g_score[(nr, nc)]:
                    g_score[(nr, nc)] = tentative_g
                    f_next = tentative_g + heuristic((nr, nc), goal)
                    heapq.heappush(pq, (f_next, nr, nc))
    return -1, visited_count

cost, total_visited = bai_24_a_star_grid()
print(f" Chi phí = {cost}, Tổng số đỉnh phải duyệt = {total_visited}")