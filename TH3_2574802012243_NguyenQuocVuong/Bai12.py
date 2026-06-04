def sap_xep_chuoi_do_dai(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # So sánh độ dài chuỗi
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


a = ['abc', 'a', 'ab']
print( sap_xep_chuoi_do_dai(a))  