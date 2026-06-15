"""
Bài 7: Sắp xếp mảng ký tự
Dùng selection sort sắp xếp một mảng ký tự theo bảng chữ cái.

Ví dụ: a = ['d','a','c','b'] -> ['a','b','c','d']
"""


def selection_sort_chars(a):
    # Python so sánh ký tự theo mã ASCII/Unicode, nên logic giống sort số
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    print(selection_sort_chars(['d', 'a', 'c', 'b']))  # ['a', 'b', 'c', 'd']
