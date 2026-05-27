def tim_kiem_ma_tran(matrix, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == x:
                return (i, j)
    return (-1, -1)

M = [[5, 8, 1], [3, 9, 7], [2, 6, 4]]
x = 9
print("Vị trí (dòng, cột):", tim_kiem_ma_tran(M, x))