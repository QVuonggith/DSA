def tim_chuoi(ds, ten):

    for i in range(0, len(ds)):
        if ds[i].lower() == ten.lower():
            return i

    return -1


ds = ["An", "Binh", "Chau"]

x = "an"

result = tim_chuoi(ds, x)

print("Output :", result)