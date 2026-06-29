import random
def insertion_sort_analyze(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        

        while j >= 0:
            comparisons += 1 
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
                
        arr[j + 1] = key
        if j + 1 != i:
            shifts += 1
            
    return comparisons, shifts


n_size = 1000


best_input = list(range(n_size))


worst_input = list(range(n_size, 0, -1))


average_input = [random.randint(1, 10000) for _ in range(n_size)]

comp_b, shift_b = insertion_sort_analyze(best_input)
comp_w, shift_w = insertion_sort_analyze(worst_input)
comp_a, shift_a = insertion_sort_analyze(average_input)

print(f"{'Trường hợp (Case)':<25} | {'Số phép so sánh':<18} | {'Số phép Shift':<15} | {'Độ phức tạp lý thuyết'}")
print("-" * 85)
print(f"{'Best (Đã sắp xếp)':<25} | {comp_b:<18} | {shift_b:<15} | O(n)")
print(f"{'Average (Ngẫu nhiên)':<25} | {comp_a:<18} | {shift_a:<15} | O(n^2)")
print(f"{'Worst (Xếp ngược)':<25} | {comp_w:<18} | {shift_w:<15} | O(n^2)")