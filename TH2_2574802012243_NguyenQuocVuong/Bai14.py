def tim_trong_ma_tran_2d(matrix, x):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // cols][mid % cols]
        if mid_val == x:
            return True
        elif mid_val < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

print(tim_trong_ma_tran_2d([[1, 3, 5], [7, 9, 11]], 9))