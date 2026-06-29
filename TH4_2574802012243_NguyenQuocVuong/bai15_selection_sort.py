def partial_selection_sort_k_smallest(a, k):
    a = a[:]
    n = len(a)
    k = min(k, n - 1) if n > 0 else 0
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    print(partial_selection_sort_k_smallest([5, 3, 1, 4, 2], 2))  
