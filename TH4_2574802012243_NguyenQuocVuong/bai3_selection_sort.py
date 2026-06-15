"""
Bài 3: Sắp xếp giảm dần
Cài đặt selection sort theo thứ tự giảm dần (mỗi vòng chọn phần tử lớn nhất).

Ví dụ: a = [5, 2, 4, 6, 1] -> [6, 5, 4, 2, 1]
"""


def selection_sort_descending(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a


if __name__ == "__main__":
    print(selection_sort_descending([5, 2, 4, 6, 1]))  # [6, 5, 4, 2, 1]
