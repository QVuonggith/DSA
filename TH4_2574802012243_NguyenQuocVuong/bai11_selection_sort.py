def selection_sort_by_key(a):
    arr = a[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    original = [(2, 'a'), (2, 'b'), (1, 'c')]
    result = selection_sort_by_key(original)
    print("Ban đầu :", original)
    print("Sau sort:", result)