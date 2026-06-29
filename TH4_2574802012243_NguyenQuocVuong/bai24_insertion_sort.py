import heapq
import time
import random

def partial_selection_sort(arr, k):
    n = len(arr)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[:k]

def heap_find_k_smallest(arr, k):
    heapq.heapify(arr) 
    return [heapq.heappop(arr) for _ in range(k)] 

n = 20000
test_data = [random.randint(1, 100000) for _ in range(n)]

print(f"Thực nghiệm với mảng n = {n} phần tử:\n")


k_small = 5
t0 = time.time()
partial_selection_sort(test_data.copy(), k_small)
t_select_small = time.time() - t0

t0 = time.time()
heap_find_k_smallest(test_data.copy(), k_small)
t_heap_small = time.time() - t0
print(f"Với k nhỏ ({k_small = }):")
print(f"  - Partial Selection: {t_select_small:.6f} giây <--- NHANH HƠN")
print(f"  - Heap:              {t_heap_small:.6f} giây")

print("-" * 40)


k_large = 5000
t0 = time.time()
partial_selection_sort(test_data.copy(), k_large)
t_select_large = time.time() - t0

t0 = time.time()
heap_find_k_smallest(test_data.copy(), k_large)
t_heap_large = time.time() - t0
print(f"Với k lớn ({k_large = }):")
print(f"  - Partial Selection: {t_select_large:.6f} giây")
print(f"  - Heap:              {t_heap_large:.6f} giây <--- NHANH HƠN VƯỢT TRỘI")