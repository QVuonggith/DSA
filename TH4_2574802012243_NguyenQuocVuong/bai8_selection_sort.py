def find_min_index_in_range(a, i):
    n = len(a)
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx


if __name__ == "__main__":
    print(find_min_index_in_range([9, 3, 7, 1, 5], 1))
