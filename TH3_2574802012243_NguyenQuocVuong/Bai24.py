def find_minimum_passes(initial, current):
    max_left_shift = 0
    for current_idx, value in enumerate(current):
        # Tìm vị trí ban đầu của phần tử này
        initial_idx = initial.index(value)
        # Nếu vị trí ban đầu nằm bên phải vị trí hiện tại -> nó đã bị dịch sang trái
        if initial_idx > current_idx:
            shift = initial_idx - current_idx
            if shift > max_left_shift:
                max_left_shift = shift
    return max_left_shift

dau = [4, 3, 2, 1]
sau = [3, 2, 1, 4]
print(  {find_minimum_passes(dau, sau)})
