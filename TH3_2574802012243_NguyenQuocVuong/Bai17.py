def sap_xep_mot_phan_k(arr, k):
    n = len(arr)
    for i in range(k):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test ví dụ
a = [3, 1, 4, 1, 5]
k = 2
print(sap_xep_mot_phan_k(a, k)) 