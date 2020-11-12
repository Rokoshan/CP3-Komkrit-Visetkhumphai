from tkinter import *
import math

# Event เมื่อมีการคลิกให้คำนวณ BMI และ เช็คค่ากับ IF และแสดงค่าเป็นช่วงน้ำหนัก
def leftClickButton(event):
    try:
        result = float(textBoxWeight.get())/(math.ceil(math.pow(float(textBoxHeight.get())/100, 2)))
        if result > 30:
            labelResult.configure(text="อ้วนมาก")
        elif result >= 25:
            labelResult.configure(text="อ้วน")
        elif result >= 23:
            labelResult.configure(text="น้ำหนักเกิน")
        elif result >= 18.6:
            labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
        elif result <= 18.5:
            labelResult.configure(text="ผอมเกินไป")
    except ValueError: # สำหรับตรวจสอบ Error ในกรณีที่มีการไม่ใส่ข้อมูลทำให้โปรแกรมไมทำงาน
        labelResult.configure(text="กรุณากรอกข้อมูล")


# ส่วนแสดง GUI เพื่อให้กรอกข้อมูล
MainWindow = Tk()
MainWindow.config(bg="pink")
MainWindow.option_add("*font", "Tahoma 9")
MainWindow.option_add("*background", "pink")
labelHeight = Label(MainWindow, text="ส่วนสูง (cm)").grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (kg)").grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()
