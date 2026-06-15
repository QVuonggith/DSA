"""
Bài 20: Liên hệ với heap sort
Heap sort có thể coi là selection sort cải tiến: thay vì quét O(n) tìm
max, dùng heap lấy max trong O(log n). Trình bày mối liên hệ và độ
phức tạp O(n log n).

Ví dụ: selection O(n^2) -> heap sort O(n log n)
"""

import heapq


def selection_sort_descending(a):
    """
    Selection sort "kiểu lấy max": mỗi vòng quét O(n) để tìm phần tử
    lớn nhất, đặt vào vị trí cuối còn lại. Tổng: O(n^2).
    """
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a


def heap_sort_demo(a):
    """
    Heap sort: xây heap một lần (O(n)), sau đó mỗi lần lấy phần tử
    nhỏ nhất/lớn nhất chỉ tốn O(log n) thay vì O(n).
    Tổng: O(n) + n * O(log n) = O(n log n).
    """
    h = a[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print("Selection sort (O(n^2)):", selection_sort_descending(arr))
    print("Heap sort (O(n log n)) :", heap_sort_demo(arr))

    # Mối liên hệ:
    # - Cả hai đều dựa trên ý tưởng "lặp lại việc chọn ra phần tử nhỏ
    #   nhất/lớn nhất còn lại và đặt vào đúng vị trí".
    # - Selection sort: tìm phần tử đó bằng cách quét tuyến tính O(n)
    #   -> tổng O(n^2).
    # - Heap sort: duy trì một cấu trúc heap để việc lấy ra phần tử
    #   nhỏ nhất/lớn nhất chỉ tốn O(log n) -> tổng O(n log n).
