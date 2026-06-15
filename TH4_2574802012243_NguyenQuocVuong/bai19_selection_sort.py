"""
Bài 19: Double-ended selection - phân tích
Phân tích kỹ bản double selection (bài 9): số vòng, số so sánh, các
trường hợp biên khi min và max trùng vị trí hoán đổi. Chứng minh tính
đúng đắn.

Ví dụ: xử lý cẩn thận khi maxIdx = vị trí đầu
"""


def analyze_double_selection_sort(a):
    """
    Phân tích:
    - Số vòng lặp = ceil(n/2) (mỗi vòng cố định 2 phần tử: 1 đầu, 1 cuối,
      trừ vòng cuối nếu n lẻ chỉ còn 1 phần tử giữa).
    - Mỗi vòng quét đoạn [left, right] (kích thước m = right-left+1),
      thực hiện 2*(m-1) phép so sánh (1 cho min, 1 cho max, với mỗi
      phần tử từ left+1 đến right).

    Trường hợp biên (correctness):
    - Nếu phần tử lớn nhất (max) đang ở đúng vị trí `left`, sau khi ta
      swap a[left] với a[min_idx] (đưa min về đầu), thì giá trị max đó
      đã bị "chuyển" sang vị trí min_idx. Nếu không cập nhật lại
      max_idx = min_idx trước khi swap a[right] với a[max_idx], ta sẽ
      vô tình lấy nhầm giá trị min (vừa được đưa tới `left`) đem ra cuối
      -> sai kết quả.
    - Khi min_idx == max_idx (chỉ xảy ra khi left == right, tức đoạn còn
      1 phần tử) thì vòng while đã dừng (left < right là False) nên
      không phát sinh xung đột.
    """
    a = a[:]
    n = len(a)
    left, right = 0, n - 1
    rounds = 0
    comparisons = 0

    while left < right:
        rounds += 1
        min_idx, max_idx = left, left
        for j in range(left + 1, right + 1):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
            comparisons += 1
            if a[j] > a[max_idx]:
                max_idx = j

        a[left], a[min_idx] = a[min_idx], a[left]

        if max_idx == left:  # trường hợp biên
            max_idx = min_idx

        a[right], a[max_idx] = a[max_idx], a[right]

        left += 1
        right -= 1

    return a, rounds, comparisons


if __name__ == "__main__":
    sorted_a, rounds, comparisons = analyze_double_selection_sort([5, 1, 4, 2, 8])
    print("Kết quả   :", sorted_a)
    print("Số vòng   :", rounds)        # ceil(5/2) = 3
    print("Số so sánh:", comparisons)

    # Test trường hợp biên: max nằm đúng tại vị trí left
    sorted_b, _, _ = analyze_double_selection_sort([9, 1, 2, 3, 4])
    print("Trường hợp biên (max ở đầu):", sorted_b)  # [1, 2, 3, 4, 9]
