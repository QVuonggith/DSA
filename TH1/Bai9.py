def tim_tat_ca(a, x):
    res = []
    for i in range(len(a)):
        if a[i] == x:
            res.append(i)
    return res