from tabulate import tabulate
class HouseholdBill:
    def __init__(self,id,owner_name,address,electric_usage,electric_price,water_usage,water_price,service_fee):
        self.id = id
        self.owner_name = owner_name
        self.address = address
        self.electric_usage = electric_usage
        self.electric_price = electric_price
        self.water_usage = water_usage
        self.water_price = water_price
        self.service_fee = service_fee

        self.total_bill = 0
        self.bill_type = ""

        self.calculate_total_bill()
        self.classify_bill()

    def calculate_total_bill(self):
        self.total_bill = self.electric_usage * self.electric_price + self.water_usage * self.water_price + self.service_fee
    def classify_bill(self):
        if self.total_bill > 3_000_000:
            self.bill_type = "Rất cao"
        elif 1_500_000 <= self.total_bill < 3_000_000:
            self.bill_type = "Cao"
        elif 500_000 <= self.total_bill < 1_500_000:
            self.bill_type = "Trung bình"
        else:
            self.bill_type = "Thấp"
class HouseholdBillManager:
    def __init__(self):
        self.bills = []
    def find_by_id(self, id):
        for bill in self.bills:
            if bill.id == id:
                return bill
        return None
    def show_all(self):
        if not self.bills :
            print("Danh sách hóa đơn điện nước đang rỗng!")
            return
        data = []
        for bill in self.bills:
            data.append([
                bill.id,
                bill.owner_name,
                bill.address,
                bill.electric_usage,
                bill.electric_price,
                bill.water_usage,
                bill.water_price,
                bill.service_fee,
                bill.total_bill,
                bill.bill_type
            ])
        headers = [
            "Mã hộ gia đình",
            "Tên chủ hộ",
            "Địa chỉ",
            "Số điện",
            "Đơn giá điện",
            "Số nước",
            "Đơn giá nước",
            "Phí dịch vụ",
            "Tổng tiền",
            "Phân loại chi phí"
        ]
        print(tabulate(data,headers = headers, tablefmt= "github"))
    def add_bill(self):
        while True:
            id = input("nhập mã hộ gia đình: ").strip()
            if not id:
                print("mã không được để trống")
                continue
            if self.find_by_id(id):
                print("mã đã tồn tại")
                continue
            break
        while True:
            name = input("nhập tên chủ hộ: ").strip()
            if not name:
                print("không được để trống tên")
                continue
            break
        address = input("nhập địa chỉ: ")
        electric_usage = input_usage("nhập số điện: ")
        electric_price = input_usage("nhập số tiền: ")
        water_usage = input_usage("nhập số nước: ")
        water_price = input_usage("nhập số tiền nước: ")
        service_fee = input_usage("nhập giá dịch vụ: ")
        bill = self.bills(
            id,
            name,
            address,
            electric_usage,
            electric_price,
            water_usage,
            water_price,
            service_fee
        )
        self.bills.append(bill)
        print("thêm thành công")
    def update_bill(self):
        id = input("Nhap ma ho gia đình: ").strip()
        bill = self.find_by_id(id)
        if not bill:
            print("Khong tim thay hộ gia đình cần cập nhật")
            return
        bill.address = input("nhập địa chỉ moi: ")
        bill.electric_usage = input_usage("nhập số điện mới: ")
        bill.electric_price = input_usage("nhập số tiền mới: ")
        bill.water_usage = input_usage("nhập số nước mới: ")
        bill.water_price = input_usage("nhập số tiền nước mới: ")
        bill.service_fee = input_usage("nhập giá dịch vụ mới: ")
        bill.total_bill()
        bill.bill_type()
        print("Cap nhat thành cong")
    def delete_bill(self):
        id = input("Nhap ma hộ gia đình: ").strip()
        bill = self.find_by_id(id)
        if not bill:
            print("Khong tim thay hộ gia đình can xoa")
            return
        confirm = input("Ban co chac muon xoa hộ gia đình nay khong (Y - N): ").strip()
        if confirm.lower() == "y":
            self.bills.remove(bill)
            print("Xoa hộ gia đình thanh cong")
        elif confirm.lower() == "n":
            print("Da huy thao tac xoa")
        else:
            print("Lua chon khong hop le")
    def search_bill(self):
        keyword = input("Nhap tu khoa tim kiem: ").strip().lower()
        result = []
        for bill in self.bills:
            if keyword in bill.name.lower():
                result.append([
                    bill.id,
                    bill.owner_name,
                    bill.address,
                    bill.electric_usage,
                    bill.electric_price,
                    bill.water_usage,
                    bill.water_price,
                    bill.service_fee,
                    bill.total_bill,
                    bill.bill_type
                ])
        if not result:
            print("Khong tim thay hộ gia đình phu hop")
            return
        headers = [
            "Mã hộ gia đình",
            "Tên chủ hộ",
            "Địa chỉ",
            "Số điện",
            "Đơn giá điện",
            "Số nước",
            "Đơn giá nước",
            "Phí dịch vụ",
            "Tổng tiền",
            "Phân loại chi phí"
        ]
        print(tabulate(result, headers=headers, tablefmt="github"))
def input_usage(message):
    while True:
        try:
            usage = float(input(message))
            if usage >= 0:
                return usage
            print("Số đã sử dụng phải lớn hơn hoặc bằng 0")
        except ValueError:
            print("nhap dung dinh dang so")
a = HouseholdBillManager()
if __name__ == "__main__":
    while True:
        choice = input("""
        ================ MENU ================
        1. Hiển thị danh sách hóa đơn điện nước
        2. Thêm hóa đơn điện nước mới
        3. Cập nhật hóa đơn điện nước
        4. Xóa hóa đơn điện nước
        5. Tìm kiếm hóa đơn
        6. Thoát
        =====================================
        Nhập lựa chọn của bạn: 
        """)
        match choice:
            case "1":
                a.show_all()
            case "2":
                a.add_bill()
            case "3":
                a.update_bill()
            case "4":
                a.delete_bill()
            case "5":
                a.search_bill()
            case "6":
                print("thoát")
                break
            case _:
                print("không hợp lệ")
                break
        

