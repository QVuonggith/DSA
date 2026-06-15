"""
Bài 4: In mảng sau mỗi vòng chọn
Sau mỗi vòng (đặt xong phần tử nhỏ thứ i), in trạng thái mảng.
Phần đầu mảng đã được sắp xếp cố định.

Ví dụ: a = [3, 1, 2] -> in [1,3,2] rồi [1,2,3]
"""


def selection_sort_print_each_round(a):
    a = a[:]
    n = len(a)
    print(f"Ban đầu: {a}")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Sau vòng {i + 1}: {a}")
    return a


if __name__ == "__main__":
    selection_sort_print_each_round([3, 1, 2])
