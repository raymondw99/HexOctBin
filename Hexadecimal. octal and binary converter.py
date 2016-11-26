from tkinter import *

root = Tk()
root.title("Hexadecimal_Octal_Binary_Converter")
root.geometry('360x270')
root.resizable(width=False, height=False)

#Clear command
def clear():
    Decimaldisplay.delete(0,END)
    Hexadecimaldisplay.delete(0,END)
    Octaldisplay.delete(0, END)
    Binarydisplay.delete(0, END)

#Conversions from decimal
def dec_convert():
    #Decimal to hexadecimal
    decimal = Decimaldisplay.get()
    if True in [f == '0' or f == '1' or f == '2' or f == '3'
                 or f == '4' or f == '5' or f == '6' or f == '7'
                 or f == '8' or f == '9' for f in decimal]:
        if decimal == '0':
           Octaldisplay.delete(0, END)
           Octaldisplay.insert(INSERT, '0')
           Hexadecimaldisplay.delete(0, END)
           Hexadecimaldisplay.insert(INSERT, '0')
           Binarydisplay.delete(0, END)
           Binarydisplay.insert(INSERT, '0')             
        else:
            hexnum = '0123456789abcdef'
            decnum = int(decimal)
            result = ''
            while (decnum>0):
                rest = (decnum%16)
                decnum = (decnum-rest)//16
                num = hexnum[rest]
                result = num + result
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, dec_to_oct(decimal))
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, result)
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, dec_to_bin(decimal))        
    else:
        if decimal == '':
           Octaldisplay.delete(0, END)
           Octaldisplay.insert(INSERT, '')
           Hexadecimaldisplay.delete(0, END)
           Hexadecimaldisplay.insert(INSERT, '')
           Binarydisplay.delete(0, END)
           Binarydisplay.insert(INSERT, '')            
        else:
           Octaldisplay.delete(0, END)
           Octaldisplay.insert(INSERT, 'Error')
           Hexadecimaldisplay.delete(0, END)
           Hexadecimaldisplay.insert(INSERT, 'Error')
           Binarydisplay.delete(0, END)
           Binarydisplay.insert(INSERT, 'Error')

#Decimal to octal
def dec_to_oct(decimal):
    decimal = Decimaldisplay.get()
    decnum = int(decimal)
    octal=[]
    while (decnum>0):
        b= int(decnum%8)
        octal.append(b)
        decnum=(decnum-b)/8
    octal_convert=""
    for j in octal[::-1]:
        octal_convert=octal_convert+str(j)
    return octal_convert

#Decimal to binary   
def dec_to_bin(decimal):
    decimal = Decimaldisplay.get()
    decnum = int(decimal)
    binary=[]
    while (decnum>0):
        a= int(decnum%2)
        binary.append(a)
        decnum=(decnum-a)/2
    bin_convert=""
    for j in binary[::-1]:
        bin_convert=bin_convert+str(j)
    return bin_convert

#Conversions from hexadecimal
def hex_convert():
    #Hexadecimal to decimal
    try:
        hexadecimal = Hexadecimaldisplay.get()
        if False in [f == '0' or f == '1' or f == '2' or f == '3'
                     or f == '4' or f == '5' or f == '6' or f == '7'
                     or f == '8' or f == '9' or f == 'a' or f == 'b'
                     or f == 'c' or f == 'd' or f == 'e' or f == 'f'
                     for f in hexadecimal]: 
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, 'Error')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, 'Error')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, 'Error')      
        else:
            hexdict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
                       "6":6, "7":7, "8":8, "9":9, "a":10, "b":11,
                       "c":12, "d":13, "e":14, "f":15}
            i = 0
            power = len(hexadecimal)
            decimal = 0
            while i < len(hexadecimal):
                    decimal = hexdict.get(hexadecimal[i])*16**(power-1)+decimal
                    i += 1
                    power -= 1
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, decimal)
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, hex_to_dec_to_oct(hexadecimal))
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, hex_to_dec_to_bin(hexadecimal))
    except UnboundLocalError:
        if hexadecimal == '0':
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '0')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, '0')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, '0')
        else:
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, '')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, '')
                
#Hexadecimal to octal
def hex_to_dec_to_oct(hexadecimal):
    hexadecimal = Hexadecimaldisplay.get()
    hexdict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
                       "6":6, "7":7, "8":8, "9":9, "a":10, "b":11,
                   "c":12, "d":13, "e":14, "f":15}
    i = 0
    power = len(hexadecimal)
    decimal = 0
    while i < len(hexadecimal):
        decimal = hexdict.get(hexadecimal[i])*16**(power-1)+decimal
        i += 1
        power -= 1
    octal=[]
    while (decimal > 0):
        b=int(decimal%8)
        octal.append(b)
        decimal=(decimal-b)/8
        octal_convert=""
        for j in octal[::-1]:
            octal_convert=octal_convert+str(j)
    return octal_convert

#Hexadecimal to binary
def hex_to_dec_to_bin(hexadecimal):
    hexadecimal = Hexadecimaldisplay.get()
    hexdict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
                       "6":6, "7":7, "8":8, "9":9, "a":10, "b":11,
                       "c":12, "d":13, "e":14, "f":15}
    i = 0
    power = len(hexadecimal)
    decimal = 0
    while i < len(hexadecimal):
        decimal = hexdict.get(hexadecimal[i])*16**(power-1)+decimal
        i += 1
        power -= 1
    binary=[]
    while (decimal > 0): 
        a=int(decimal%2)
        binary.append(a)
        decimal=(decimal-a)/2
        bin_convert=""
        for j in binary[::-1]:
            bin_convert=bin_convert+str(j)
    return bin_convert

#Conversions from octal
def oct_convert():
    #Octal to decimal
    try:
        octal = Octaldisplay.get()
        if False in [f == '0' or f == '1' or f == '2' or f == '3'
                     or f == '4' or f == '5' or f == '6' or f == '7'
                     for f in octal]: 
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, 'Error')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, 'Error')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, 'Error')  
        else:
           decimal = 0
           for digit in octal:
               decimal = decimal*8 + int(digit)
           Decimaldisplay.delete(0, END)
           Decimaldisplay.insert(INSERT, decimal)
           Hexadecimaldisplay.delete(0, END)
           Hexadecimaldisplay.insert(INSERT, oct_to_dec_to_hex())
           Binarydisplay.delete(0, END)
           Binarydisplay.insert(INSERT, oct_to_dec_to_bin())
    except UnboundLocalError:
        if octal == '0':
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '0')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, '0')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, '0')             
        else:
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, '')
            Binarydisplay.delete(0, END)
            Binarydisplay.insert(INSERT, '')
            
#Octal to hexadecimal
def oct_to_dec_to_hex():
    octal = Octaldisplay.get()
    decimal = 0
    for digit in octal:
        decimal = decimal*8 + int(digit)
    hexnum = '0123456789abcdef'
    result = ''
    while (decimal>0):
        rest = (decimal%16)
        decimal = (decimal-rest)//16
        num = hexnum[rest]
        result = num + result
    return result

#Octal to binary
def oct_to_dec_to_bin():
    octal = Octaldisplay.get()
    decimal = 0
    for digit in octal:
        decimal = decimal*8 + int(digit)
    binary=[]
    while (decimal > 0): 
        a=int(decimal%2)
        binary.append(a)
        decimal=(decimal-a)/2
        bin_convert=""
        for j in binary[::-1]:
            bin_convert=bin_convert+str(j)
    return bin_convert

#Conversions from binary
def bin_convert():
    #Binary to decimal
    try:
        binary = Binarydisplay.get()
        if False in [f == '0' or f == '1' for f in binary]:
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, 'Error')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, 'Error')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, 'Error')  
        else:
           decimal = 0
           for digit in binary:
               decimal = decimal*2 + int(digit)
           Decimaldisplay.delete(0, END)
           Decimaldisplay.insert(INSERT, decimal)
           Hexadecimaldisplay.delete(0, END)
           Hexadecimaldisplay.insert(INSERT, bin_to_dec_to_hex())
           Octaldisplay.delete(0, END)
           Octaldisplay.insert(INSERT, bin_to_dec_to_oct())
    except UnboundLocalError:
        if binary == '0':
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '0')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, '0')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, '0')             
        else:
            Decimaldisplay.delete(0, END)
            Decimaldisplay.insert(INSERT, '')
            Hexadecimaldisplay.delete(0, END)
            Hexadecimaldisplay.insert(INSERT, '')
            Octaldisplay.delete(0, END)
            Octaldisplay.insert(INSERT, '')
            
#Binary to hexadecimal
def bin_to_dec_to_hex():
    binary = Binarydisplay.get()
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    hexnum = '0123456789abcdef'
    result = ''
    while (decimal>0):
        rest = (decimal%16)
        decimal = (decimal-rest)//16
        num = hexnum[rest]
        result = num + result
    return result

#Binary to octal
def bin_to_dec_to_oct():
    binary = Binarydisplay.get()
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    octal=[]
    while (decimal>0):
        b=int(decimal%8)
        octal.append(b)
        decimal=(decimal-b)/8
        octal_convert=""
    for j in octal[::-1]:
        octal_convert=octal_convert+str(j)
    return octal_convert
           
#Title
Title = Label(root, text= "Hexadecimal, Octal and Binary Converter", font = ('Avenir', 18, 'normal'))
Title.grid(column = 0, columnspan = 7, padx = 5, pady = 5)

#Entry Boxes
Decimal = Label(root, text = "Decimal:", font = ('Avenir', 15, 'normal'))
Decimal.grid(row = 1, sticky = W, padx = 4)
Decimaldisplay = Entry(root)
Decimaldisplay.grid(row = 1, column = 1, sticky = E, pady = 0, padx = 0)
Convert1 = Button(root, text = "Convert", command = dec_convert, font = ('Avenir', 15, 'normal'))
Convert1.grid(row = 1, column = 3, sticky = E, pady = 0, padx = 0)

Hexadecimal = Label(root, text="Hexadecimal:", font = ('Avenir', 15, 'normal'))
Hexadecimal.grid(row = 2, sticky = W, padx = 4)
Hexadecimaldisplay = Entry(root)
Hexadecimaldisplay.grid(row = 2, column = 1, sticky = E, pady = 0, padx = 0)
Convert2 = Button(root, text = "Convert", command = hex_convert, font = ('Avenir', 15, 'normal'))
Convert2.grid(row = 2, column = 3, sticky = E, pady = 0, padx = 0)

Octal = Label(root, text = "Octal:", font = ('Avenir', 15, 'normal'))
Octal.grid(row = 3, sticky = W, padx = 4)
Octaldisplay = Entry(root)
Octaldisplay.grid(row = 3, column = 1, sticky = E, pady = 0, padx = 0)
Convert3 = Button(root, text = "Convert", command = oct_convert, font = ('Avenir', 15, 'normal'))
Convert3.grid(row = 3, column = 3, sticky = E, pady = 0, padx = 0)

Binary = Label(root, text="Binary:", font = ('Avenir', 15, 'normal'))
Binary.grid(row = 4, sticky = W, padx = 4)
Binarydisplay = Entry(root)
Binarydisplay.grid(row = 4, column = 1, sticky = E, pady = 0, padx = 0)
Convert4 = Button(root, text = "Convert", command = bin_convert, font = ('Avenir', 15, 'normal'))
Convert4.grid(row = 4, column = 3, sticky = E, pady = 0, padx = 0)

#Clear Button
clear = Button(text = "Clear", command = clear, font = ('Avenir', 15, 'normal'))
clear.grid(row = 5, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#Exit Button
Exit = Button(text = 'Exit', command = root.destroy, font = ('Avenir', 15, 'normal'))
Exit.grid(row = 6, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#Credits
Credits = Label(root, text = "Raymond Wang 2016 ®", font = ('Avenir', 15, 'italic'))
Credits.grid(row = 7, column = 0, columnspan = 7, pady = 5, padx = 5)

root.mainloop()
