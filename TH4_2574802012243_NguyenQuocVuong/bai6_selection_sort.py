def selection_sort_count_comparisons(a):
    a = a[:]
    n = len(a)
    comparisons = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    expected = n * (n - 1) // 2
    return a, comparisons, expected


if __name__ == "__main__":
    sorted_a, comparisons, expected = selection_sort_count_comparisons([4, 1, 3, 2, 5])
    print(sorted_a)
    print("Số so sánh:", comparisons, "| n(n-1)/2 =", expected)
