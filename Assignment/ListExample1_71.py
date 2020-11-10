menuList = []
priceList = []


def showReceipt():
    print("----My Food----")
    for number in range(len(menuList)):
        print("ชื่อรายการ : %s ราคา   %d" % (menuList[number], priceList[number]))


def totalPrice():
    price = 0
    for i in priceList:
        price += i

    print("----------------------")
    print("Total : ", price, "บาท")


while True:
    menuName = input("Please Enter Your Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showReceipt()
totalPrice()
