def so_nguyen_to(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def tim_snt(a):

    for i in range(0, len(a)):
        if so_nguyen_to(a[i]):
            return i

    return -1


a = [4, 6, 9, 7, 11]

result = tim_snt(a)

print("Output :", result)