import random


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


def analyze_best_average_worst_case(n=10, seed=42):
    random.seed(seed)
    sorted_arr = list(range(n))             
    reverse_arr = list(range(n, 0, -1))     
    random_arr = sorted_arr[:]
    random.shuffle(random_arr)               

    cases = {
        "Đã sắp xếp (best)": sorted_arr,
        "Ngẫu nhiên (average)": random_arr,
        "Sắp xếp ngược (worst)": reverse_arr,
    }

    results = {}
    for name, arr in cases.items():
        _, comparisons, expected = selection_sort_count_comparisons(arr)
        _, swaps = selection_sort_count_actual_swaps(arr)
        results[name] = {
            "array": arr,
            "comparisons": comparisons,
            "expected_comparisons": expected,
            "swaps": swaps,
        }
    return results


if __name__ == "__main__":
    for name, info in analyze_best_average_worst_case(n=8).items():
        print(name, "->", info)
 