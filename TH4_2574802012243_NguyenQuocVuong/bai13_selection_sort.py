"""
Bài 13: Sắp xếp đối tượng theo khóa
Sắp danh sách học sinh theo điểm tăng dần bằng selection sort.

Ví dụ: [('An',8),('Ba',5)] -> [('Ba',5),('An',8)]
"""


def sort_students_by_score(students):
    arr = students[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    print(sort_students_by_score([('An', 8), ('Ba', 5)]))  # [('Ba', 5), ('An', 8)]
