def on_dinh(arr):
    n = len(arr)
    res = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j][0] > res[j + 1][0]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

def ko_on_dinh(arr):
    n = len(arr)
    res = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j][0] >= res[j + 1][0]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

data = [(2, 'Nhãn A'), (1, 'Nhãn B'), (2, 'Nhãn C')]
print(on_dinh(data))   
print(ko_on_dinh(data))     
