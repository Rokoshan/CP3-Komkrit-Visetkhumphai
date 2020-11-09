num = int(input())
text = ""

for i in range(num):
    if i == 0:
        text += "*"
        print(" "*num, text)
    else:
        text += "*"*2
        print(" "*(num-i), text)