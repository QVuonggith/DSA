"""
Bài 9: Double selection sort
Cải tiến: mỗi vòng tìm cả phần tử nhỏ nhất và lớn nhất, đặt nhỏ nhất về
đầu và lớn nhất về cuối. Giảm số vòng còn một nửa. So sánh số so sánh
với bản thường.

Ví dụ: a = [5, 1, 4, 2, 8] -> [1, 2, 4, 5, 8]
"""


def double_selection_sort(a):
    a = a[:]
    n = len(a)
    left, right = 0, n - 1
    comparisons = 0

    while left < right:
        min_idx, max_idx = left, left
        for j in range(left + 1, right + 1):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
            comparisons += 1
            if a[j] > a[max_idx]:
                max_idx = j

        # Đưa min về đầu (left)
        a[left], a[min_idx] = a[min_idx], a[left]

        # Trường hợp đặc biệt: nếu max nằm ở vị trí "left" ban đầu,
        # sau khi swap min ở trên nó đã bị đổi sang vị trí min_idx
        if max_idx == left:
            max_idx = min_idx

        # Đưa max về cuối (right)
        a[right], a[max_idx] = a[max_idx], a[right]

        left += 1
        right -= 1

    return a, comparisons


if __name__ == "__main__":
    sorted_a, comparisons = double_selection_sort([5, 1, 4, 2, 8])
    print(sorted_a, "- số so sánh:", comparisons)  # [1, 2, 4, 5, 8]
