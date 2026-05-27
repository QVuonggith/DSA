def tim_so_chan(a):

    for i in range(0, len(a)):
        if a[i] % 2 == 0:
            return i

    return -1


a = [3, 7, 11, 8, 5, 4]

result = tim_so_chan(a)

print("Output :", result)