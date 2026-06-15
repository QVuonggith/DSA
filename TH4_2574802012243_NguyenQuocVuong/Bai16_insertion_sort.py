def insertion_sort(luong):
    a = []  
    
    for item in luong:
        a.append(item)  
        
        key = a[-1]
        j = len(a) - 2
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

        print(a)

b = [5, 2, 8, 1]
insertion_sort(b)