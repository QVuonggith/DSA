def analyze_bubble_sort(arr):
    n = len(arr)
    res = list(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return {"So sanh": comparisons, "Swap": swaps}

best_case = [1, 2, 3, 4, 5]
worst_case = [5, 4, 3, 2, 1]
avg_case = [3, 1, 5, 2, 4]

print(analyze_bubble_sort(best_case))  
print( analyze_bubble_sort(worst_case)) 
print( analyze_bubble_sort(avg_case))   
print("\n> BẢNG TÓM TẮT ĐỘ PHỨC TẠP LÝ THUYẾT O(n^2):")
print("| Trường hợp  | Số lần so sánh | Số lần hoán đổi (Swap) | Độ phức tạp |")
print("|-------------|----------------|------------------------|-------------|")
print("| Best-case   | n - 1          | 0                      | O(n)        |")
print("| Worst-case  | n*(n-1)/2      | n*(n-1)/2              | O(n^2)      |")
print("| Average-case| O(n^2)         | O(n^2)                 | O(n^2)      |")
