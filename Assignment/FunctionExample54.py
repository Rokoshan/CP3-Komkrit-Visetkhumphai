# เช็ค Username และ รหัสผ่าน ถ้ากรอกผิดให้กรอกใหม่
def login():
    while True:
        usernameInput = input("Username :")
        passwordInput = input("Password :")
        if usernameInput == "admin" and passwordInput == "1234":
            return True
        else:
            print("Username หรือ รหัสผ่าน ไม่ถูกต้อง")
            print("กรุณากรอกใหม่อีกครั้ง")


# แสดงเมนูการทำงาน
def showMenu():
    print("ยินดีต้อนรับเข้าสู่ระบบ")
    print("-----Bank Shop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")


# เลือกเมนูและคืนค่าเป็นค่าเป็นตัวเลข
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected


# คำนวนภาษีโดยรับค่าเป็นตัวเลขเข้าสู่ฟังค์ชั่น
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


# คำนวนราคาพร้อม Vat
def priceCalculate():
    firstNum = int(input("First Product Price :"))
    secondNum = int(input("Second Product Price :"))
    return vatCalculate(firstNum + secondNum)


if login():
    showMenu()
    choose = menuSelect()
    if choose == 1:
        totalPrice = int(input("กรุณาใส่ราคาที่ต้องการคำนวนภาษี :"))
        print("Result :", vatCalculate(totalPrice))
    elif choose == 2:
        print("Total :", priceCalculate())
