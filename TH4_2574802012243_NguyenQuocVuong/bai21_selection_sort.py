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


def verify_comparison_formula(test_arrays):
    
    results = []
    for arr in test_arrays:
        n = len(arr)
        _, comparisons, expected = selection_sort_count_comparisons(arr)
        results.append({
            "input": arr,
            "n": n,
            "comparisons": comparisons,
            "expected_n(n-1)/2": expected,
            "match": comparisons == expected,
        })
    return results


if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],   
        [5, 4, 3, 2, 1],   
        [3, 1, 4, 5, 2],   
    ]
    for r in verify_comparison_formula(test_arrays):
        print(r)
  
