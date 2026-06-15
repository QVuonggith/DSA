"""
Bài 17: Phần tử nhỏ thứ k (partial selection)
Tìm giá trị nhỏ thứ k mà không sắp xếp toàn bộ: chỉ chạy k vòng
selection. Phân tích độ phức tạp O(n*k).

Ví dụ: a = [7, 2, 5, 1, 9], k = 3 -> 5
"""


def find_kth_smallest_partial_selection(a, k):
    a = a[:]
    n = len(a)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k - 1]


if __name__ == "__main__":
    print(find_kth_smallest_partial_selection([7, 2, 5, 1, 9], 3))  # 5
    # Độ phức tạp: O(n*k) vì chỉ chạy k vòng, mỗi vòng quét O(n)
