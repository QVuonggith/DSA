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

        a[left], a[min_idx] = a[min_idx], a[left]
        if max_idx == left:
            max_idx = min_idx

        a[right], a[max_idx] = a[max_idx], a[right]

        left += 1
        right -= 1

    return a, comparisons


if __name__ == "__main__":
    sorted_a, comparisons = double_selection_sort([5, 1, 4, 2, 8])
    print(sorted_a, "- số so sánh:", comparisons)
