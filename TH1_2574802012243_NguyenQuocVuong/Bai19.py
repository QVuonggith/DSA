danh_sach_sv = [
    {"ma_sv": "2574801", "ho_ten": "Nguyễn Văn A", "dtb": 7.5},
    {"ma_sv": "2574802", "ho_ten": "Trần Thị B", "dtb": 8.2},
    {"ma_sv": "2574803", "ho_ten": "Lê Văn C", "dtb": 6.9}
]

def tim_kiem_sinh_vien(ds, ma_can_tim):
    for sv in ds:
        if sv["ma_sv"] == ma_can_tim:
            print("--- THÔNG TIN SINH VIÊN ---")
            print("Mã SV:", sv["ma_sv"])
            print("Họ tên:", sv["ho_ten"])
            print("Điểm trung bình:", sv["dtb"])
            return
    print("Không tìm thấy sinh viên có mã:", ma_can_tim)

tim_kiem_sinh_vien(danh_sach_sv, "2574802")