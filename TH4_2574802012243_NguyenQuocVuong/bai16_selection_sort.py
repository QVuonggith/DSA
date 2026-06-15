"""
Bài 16: Sắp xếp theo trị tuyệt đối
Sắp xếp tăng dần theo |a[i]| bằng selection sort.

Ví dụ: a = [-3, 1, -2, 2] -> [1, -2, 2, -3]
"""


def selection_sort_by_absolute_value(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[min_idx]):
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    print(selection_sort_by_absolute_value([-3, 1, -2, 2]))  # [1, -2, 2, -3]
