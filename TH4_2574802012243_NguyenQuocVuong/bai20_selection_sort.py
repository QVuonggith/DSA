import heapq

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


def heap_sort_demo(a):
    h = a[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print("Selection sort (O(n^2)):", selection_sort_descending(arr))
    print("Heap sort (O(n log n)) :", heap_sort_demo(arr))