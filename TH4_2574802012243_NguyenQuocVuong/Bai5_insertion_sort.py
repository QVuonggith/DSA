def insertion_sort(a):
    count = 0  
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]  
            count += 1       
            j -= 1
            
        a[j + 1] = key
        
    print(count)

a = [3, 2, 1]
insertion_sort(a)