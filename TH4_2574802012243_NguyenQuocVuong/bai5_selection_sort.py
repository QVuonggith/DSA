"""
Bài 5: Đếm số lần hoán đổi
Sắp xếp tăng dần và đếm số lần hoán đổi. Selection sort dùng tối đa n-1 swap.

Ví dụ: a = [3, 2, 1] -> <= 2 swap
"""


def selection_sort_count_swaps(a):
    a = a[:]
    n = len(a)
    swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swap_count += 1  # mỗi vòng tính là 1 lần "hoán đổi" (tối đa n-1 lần)
    return a, swap_count


if __name__ == "__main__":
    sorted_a, swaps = selection_sort_count_swaps([3, 2, 1])
    print(sorted_a, "- số swap:", swaps)  # [1, 2, 3] - số swap: 2
