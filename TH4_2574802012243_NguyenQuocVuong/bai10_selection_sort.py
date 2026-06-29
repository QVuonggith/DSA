def selection_sort_count_actual_swaps(a):
    a = a[:]
    n = len(a)
    swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap_count += 1
    return a, swap_count


if __name__ == "__main__":
    sorted_a, swaps = selection_sort_count_actual_swaps([1, 2, 3])
    print(sorted_a, "- số swap thực tế:", swaps)