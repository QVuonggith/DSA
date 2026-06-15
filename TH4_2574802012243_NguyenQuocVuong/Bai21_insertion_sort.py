def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Con trỏ cho mảng con bên trái
    j = mid + 1 # Con trỏ cho mảng con bên phải
    k = left    # Con trỏ cho mảng tạm
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Nếu arr[i] > arr[j], thì tất cả các phần tử từ arr[i] đến arr[mid]
            # đều lớn hơn arr[j] vì mảng con bên trái đã được sắp xếp.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Sao chép các phần tử còn lại của mảng trái (nếu có)
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại của mảng phải (nếu có)
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Chép lại mảng tạm vào mảng gốc
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
        
    return inv_count

def merge_sort_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count

def count_shifts_large_array(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_count(arr, temp_arr, 0, len(arr) - 1)

# Thử nghiệm với mảng ngẫu nhiên
import random
large_arr = [random.randint(1, 100000) for _ in range(10000)]
print(f"Tổng số shift đếm được bằng O(n log n): {count_shifts_large_array(large_arr.copy())}")