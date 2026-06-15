def insertion_sort_k_steps(a, k):
    for i in range(1, k + 1):
        if i >= len(a):
            break
            
        key = a[i]
        j = i - 1
        
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            
        a[j + 1] = key
        
    print(a)

a = [4, 3, 2, 1]
k = 1
insertion_sort_k_steps(a, k)