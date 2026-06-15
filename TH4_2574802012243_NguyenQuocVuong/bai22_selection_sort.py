def stable_inplace_selection_sort(a, key=lambda x: x):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if key(a[j]) < key(a[min_idx]):
                min_idx = j

        if min_idx == i:
            continue

        min_val = a[min_idx]
        for k in range(min_idx, i, -1):
            a[k] = a[k - 1]
        a[i] = min_val
    return a


if __name__ == "__main__":
    print(stable_inplace_selection_sort([3, 1, 2]))  # [1, 2, 3]

    
    original = [(2, 'a'), (2, 'b'), (1, 'c')]
    print(stable_inplace_selection_sort(original, key=lambda x: x[0]))
    