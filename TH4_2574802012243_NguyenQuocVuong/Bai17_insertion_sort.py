def check_almost_sorted(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
        
    print(shifts)

a = [1, 2, 4, 3, 5]
check_almost_sorted(a)