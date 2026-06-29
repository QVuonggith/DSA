import heapq

def k_smallest_partial_selection(a, k):
    """O(n*k): chạy k vòng selection sort."""
    a = a[:]
    n = len(a)
    k = min(k, n)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[:k]


def k_smallest_heap(a, k):
    """O(n + k log n): dùng heapq.nsmallest (heapify rồi pop k lần)."""
    return heapq.nsmallest(k, a)


if __name__ == "__main__":
    a = [7, 2, 5, 1, 9, 3, 8, 4, 6, 0]
    for k in (1, 3, 5):
        ps = k_smallest_partial_selection(a, k)
        hp = k_smallest_heap(a, k)
        print(f"k={k}: partial_selection={ps} | heap={hp}")
    