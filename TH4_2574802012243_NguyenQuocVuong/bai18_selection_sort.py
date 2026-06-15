"""
Bài 18: So sánh số swap với bubble sort
Trên cùng tập dữ liệu, so sánh số swap của selection sort (<= n-1) với
bubble sort (bằng số nghịch thế). Giải thích sự chênh lệch.

Ví dụ: selection thường ít swap hơn bubble
"""


def selection_sort_count_actual_swaps(a):
    a = a[:]
    n = len(a)
    swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap_count += 1
    return a, swap_count


def bubble_sort_count_swaps(a):
    a = a[:]
    n = len(a)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_count += 1
    return a, swap_count


def compare_swaps_selection_vs_bubble(a):
    _, sel_swaps = selection_sort_count_actual_swaps(a)
    _, bub_swaps = bubble_sort_count_swaps(a)
    return sel_swaps, bub_swaps


if __name__ == "__main__":
    sel_swaps, bub_swaps = compare_swaps_selection_vs_bubble([5, 2, 4, 6, 1, 3])
    print("Selection sort swaps:", sel_swaps)
    print("Bubble sort swaps   :", bub_swaps)
    # Giải thích: Selection sort tối đa n-1 swap (mỗi vòng chỉ 1 swap để
    # đưa phần tử đúng vào vị trí), trong khi bubble sort cần 1 swap cho
    # MỖI cặp nghịch thế (inversion) trong mảng -> thường nhiều hơn.
