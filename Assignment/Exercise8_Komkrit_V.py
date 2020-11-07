usernameInput = input("Username :")
passwordInput = input("Password :")

username = "Komkrit"
password = "12345"

if usernameInput == username and passwordInput == password:
    print("   ยินดีต้อนรับเข้าสู่ร้านของเรา   ")
    print("------- Bank Shop -------")
    print("กรุณาเลือกรายการสินค้าที่ท่านต้องการ")
    print("1. Apple  ราคาลูกละ 10 บาท")
    print("2. Banana ราคาลูกละ 5  บาท")
    print("3. Orange ราคาลูกละ 10 บาท")
    userSelected = int(input(">>"))
    qty = 0
    if userSelected == 1:
        qty = int(input("กรุณาระบุจำนวนที่ท่านต้องการซื้อ >>"))
        print("Total = ", qty*10)
        print("ขอบคุณที่ใช้บริการ")
    elif userSelected == 2:
        qty = int(input("กรุณาระบุจำนวนที่ท่านต้องการซื้อ >>"))
        print("Total = ", qty * 5)
        print("ขอบคุณที่ใช้บริการ")
    elif userSelected == 3:
        qty = int(input("กรุณาระบุจำนวนที่ท่านต้องการซื้อ >>"))
        print("Total = ", qty * 10)
        print("ขอบคุณที่ใช้บริการ")
else:
    print("รหัสผ่าน หรือ Username ไม่ถูกต้อง")