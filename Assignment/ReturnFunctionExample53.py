def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print("Total:", vatCalculate(int(input("กรุุณาใส่สินค้าเพื่อคำนวนภาษี:"))))
