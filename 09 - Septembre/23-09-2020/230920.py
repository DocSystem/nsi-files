def dectobin(num):
    print(bin(int(num)).split('b')[1])

def dectohex(num):
    print(hex(int(num)).split('x')[1].upper())

def bintodec(num):
    print(int("0b" + str(num), 2))

def hextodec(num):
    print(int("0x" + str(num).lower(), 16))

def binaddition(num1, num2):
    print(bin(int("0b" + str(num1), 2)+int("0b" + str(num2), 2)).split('b')[1])
#binaddition(10, 10)

def binsoustraction(num1, num2):
    print(bin(int("0b" + str(num1), 2)-int("0b" + str(num2), 2)).split('b')[1])

def binmultiplication(num1, num2):
    print(bin(int("0b" + str(num1), 2)*int("0b" + str(num2), 2)).split('b')[1])

def bindivision(num1, num2):
    print(bin(int("0b" + str(num1), 2)/int("0b" + str(num2), 2)).split('b')[1])
