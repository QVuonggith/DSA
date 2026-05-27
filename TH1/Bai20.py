danh_ba = [
    {"ten": "An", "sdt": "090123456"},
    {"ten": "Bình", "sdt": "091234567"},
    {"ten": "An Nhiên", "sdt": "090987654"},
    {"ten": "Cường", "sdt": "034567890"}
]

while True:
    print("\n========= QUẢN LÝ DANH BẠ =========")
    print("1. Thêm liên hệ mới")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số liên hệ có SDT bắt đầu bằng số cho trước")
    print("0. Thoát chương trình")
    print("===================================")
    
    luachon = input("Nhập lựa chọn của bạn (0-4): ").strip()
    
    if luachon == "1":
        ten = input("Nhập tên: ").strip()
        sdt = input("Nhập số điện thoại: ").strip()
        danh_ba.append({"ten": ten, "sdt": sdt})
        print("=> Đã thêm liên hệ thành công!")
        
    elif luachon == "2":
        ten_tim = input("Nhập tên cần tìm số điện thoại: ").strip()
        found = False
        for lh in danh_ba:
            if lh["ten"].lower() == ten_tim.lower():
                print("-> Số điện thoại của", lh["ten"], "là:", lh["sdt"])
                found = True
        if not found:
            print("=> Không tìm thấy tên này trong danh bạ.")
            
    elif luachon == "3":
        sdt_tim = input("Nhập số điện thoại cần tìm tên: ").strip()
        found = False
        for lh in danh_ba:
            if lh["sdt"] == sdt_tim:
                print("-> Số điện thoại", sdt_tim, "là của:", lh["ten"])
                found = True
                break
        if not found:
            print("=> Không tìm thấy số điện thoại này trong danh bạ.")
            
    elif luachon == "4":
        dau_so = input("Nhập đầu số cần đếm (ví dụ '090'): ").strip()
        dem = 0
        print("Các liên hệ có đầu số", dau_so, ":")
        for lh in danh_ba:
            if lh["sdt"].startswith(dau_so):
                print(" -", lh["ten"], ":", lh["sdt"])
                dem += 1
        print("=> Tổng số liên hệ bắt đầu bằng '", dau_so, "' là:", dem)
        
    elif luachon == "0":
        print("Tạm biệt! Chương trình đã kết thúc.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")