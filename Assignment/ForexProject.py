from forex_python.converter import *
from datetime import *
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

c = CurrencyRates()
symbol = CurrencyCodes()
currency_name = CurrencyRates().get_rates('USD')
country = dict()
for i in currency_name:
    if i not in country:
        country[i] = CurrencyCodes().get_currency_name(i)


def show_country_name():
    print("---------------------------------------------".center(20))
    print("รายชื่อประเทศและสกุลเงิน".center(55))
    for n in country:
        print("ตัวย่อ: {}  สกุลเงิน: {}".format(n, country[n]))


def choose_menu():
    while True:
        try:
            print("--------ยินดีต้อนรับเข้าสู่โปรแกรมการคำนวณค่าเงิน---------".center(20))
            print("กรุณาเลือกเมนูสำหรับเข้าใช้งานโปรแกรม".center(55))
            print("1 >> โปรแกรมแปลงค่าเงินสกุลต่างๆ")
            print("2 >> โปรแกรมแสดงค่าเงินจากปี 2010")
            choose = int(input("กรุณาใส่ตัวเลขเพื่อเลือกโปรแกรม: "))
            return choose
        except ValueError:
            print("!!!!!กรุณากรอกค่าเป็นตัวเลขคำสั่ง!!!!!")


def currency_convert():
    show_country_name()
    while True:
        try:
            first = str(input("กรุณาใส่สกุลเงินที่ต้องการ: ").upper())
            second = str(input("กรุณาใส่สกุลเงินที่ต้องการแปลงค่า: ").upper())
            amount = int(input("จำนวนที่่ต้องการแปลงค่า: "))
            result = c.get_rate(first, second)
            result_convert = c.convert(first, second, amount)
            print("ค่าเงิน {} : {:.2f} {} : {}".format(second, result, symbol.get_symbol(second), first))
            print("Total : {:.2f} {}".format(result_convert, symbol.get_symbol(second)))
            print(symbol.get_currency_name(second))
            break
        except RatesNotAvailableError:
            print("!!!กรุณากรอกตัวย่อ 3 ตัวอักษร หรือ ตรวจสอบตัวอักษรให้ถูกต้อง!!!")


def exchange_rate_fc():
    show_country_name()
    try:
        year = int(input("กรุณาใส่ปีที่ต้องการดูข้อมูลถึง(คศ.): "))
        dt_obj = date(year, 1, 1)
        first = str(input("กรุณาใส่สกุลเงินที่ต้องการ: ").upper())
        second = str(input("กรุณาใส่สกุลเงินที่ต้องการแปลงค่า: ").upper())
        value = []
        points = []
        for t in range(2010, dt_obj.year + 1):
            forecast = c.get_rate(first, second, date(t, 1, 1))
            if t > 2021:
                break
            else:
                if forecast not in value:
                    value.append(forecast)
                    points.append(t)

        x = np.array(value)
        y = np.array(points)
        print("ค่าสูงสุดของสกุลเงินที่เปรียบเทียบ: {:.2f} {}".format(max(value), symbol.get_symbol(second)))
        print("ค่าเฉลี่ยค่าเงินของสกุลเงินที่เปรียบเทียบ: {:.2f} {}".format(mean(value), symbol.get_symbol(second)))
        plt.plot(x, y)
        plt.show()
    except RatesNotAvailableError:
        print("!!!กรุณากรอกตัวย่อ 3 ตัวอักษร หรือ ตรวจสอบตัวอักษรให้ถูกต้อง!!!")
    except ValueError:
        print("!!!กรุณากรอกตัวเลขปี คศ.!!!")


def main_program(choose):
    if choose == 1:
        currency_convert()
    elif choose == 2:
        exchange_rate_fc()


main_program(choose_menu())
