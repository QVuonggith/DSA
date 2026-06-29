def kiem_tra_sap_xep_k(arr, k):
    n = len(arr)
    for i in range(k):
        for j in range(0, n - 1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False  
            
    return True  

# Test ví dụ
print(kiem_tra_sap_xep_k([3, 2, 1], k=1))  