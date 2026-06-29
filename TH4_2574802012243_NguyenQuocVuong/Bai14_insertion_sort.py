def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0:
            condition1 = a[j][1] < key[1]
            
            condition2 = (a[j][1] == key[1]) and (a[j][0] > key[0])
            
            if condition1 or condition2:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
                
        a[j + 1] = key
        
    print(a)

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
insertion_sort(a)  