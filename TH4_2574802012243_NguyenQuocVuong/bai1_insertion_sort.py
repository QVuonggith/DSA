a = [4, 2, 7, 1, 3]

min_index = 0

for i in range(1, len(a)):
    if a[i] < a[min_index]:
        min_index = i 
a[0], a[min_index] = a[min_index], a[0]

print(a)