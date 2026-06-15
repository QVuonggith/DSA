def insertion_sort(a):
    count = 0  
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0:
            count += 1  
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break  
                
        a[j + 1] = key
        
    print(count)

a = [1, 2, 3]
insertion_sort(a)  