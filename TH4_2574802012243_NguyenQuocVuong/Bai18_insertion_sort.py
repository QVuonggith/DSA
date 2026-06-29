# Chiến lược 1: Dò từ phải sang trái (Mặc định)
def scan_right_to_left(a):
    comparisons = 0
    arr = list(a)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

def scan_left_to_right(a):
    comparisons = 0
    arr = list(a)
    for i in range(1, len(arr)):
        key = arr[i]
        insert_pos = i
        for j in range(i):
            comparisons += 1
            if arr[j] > key:
                insert_pos = j
                break
        val = arr[i]
        for k in range(i, insert_pos, -1):
            arr[k] = arr[k - 1]
        arr[insert_pos] = val
    return comparisons

a = [1, 2, 4, 3, 5]

print(scan_right_to_left(a))
print(scan_left_to_right(a))