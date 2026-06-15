def insertion_sort_descending(a):
    for i in range(1, len(a)):
        key = a[i]  
        j = i - 1
        
        
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
            
        a[j + 1] = key

a = [5, 2, 4, 6, 1]


insertion_sort_descending(a)
print(a)