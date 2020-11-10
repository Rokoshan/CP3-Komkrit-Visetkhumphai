menuList = []


def showReceipt():
    print("----My Food----")
    for number in range(len(menuList)):
        print("ชื่อรายการ : %s ราคา   %d" % (menuList[number][0], menuList[number][1]))

    # for (name, price) in menuList:
        # print("ชื่อรายการ : %s ราคา   %d" % (name, price))
    # for name in menulist:
        # for price in menulist[name]:


def totalPrice():
    price = 0
    for x in range(len(menuList)):
        price += menuList[x][1]

    print("----------------------")
    print("Total : ", price, "บาท")

    # for (x, y) in menuList:
    # price += y


while True:
    menuName = input("Please Enter Your Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName, menuPrice])


showReceipt()
totalPrice()
