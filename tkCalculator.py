try:
    from tkinter import *

except:
    print("You don't have Tkinter installed, go to the terminal or CMD and use: pip3 install tk")
    
    quit()

screen = Tk()
screen.title("Calcularor - Beta1.0.0")
screen.geometry("500x520")
screen.configure(bg="white")
screen.eval("tk::PlaceWindow . center")
screen.resizable(False, False)

digit = 1
total = ""
operation = ""
value = 0
value2 = 0

#BETA VALUE
value3 = 0
value4 = 0
value5 = 0
value6 = 0
value7 = 0
value8 = 0
value9 = 0
value10 = 0

while True:
    
    def close(event):
        quit()
    
    def one_():
        """In all number def's"""
        
        global value, value2
        
        if digit == 1:
            value = value * 10 + 1

        elif digit == 2:
            value2 = value2 * 10 + 1


        print (value)

    def two_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 2

        elif digit == 2:
            value2 = value2 * 10 + 2

        print (value)

    def three_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 3

        elif digit == 2:
            value2 = value2 * 10 + 3

        print (value)

    def four_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 4

        elif digit == 2:
            value2 = value2 * 10 + 4

        print (value)

    def five_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 5

        elif digit == 2:
            value2 = value2 * 10 + 5

        print (value)

    def six_():
        """In all number def's"""
        
        global value, value2
        if digit == 1:
            value = value * 10 + 6

        elif digit == 2:
            value2 = value2 * 10 + 6

        print (value)

    def seven_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 7

        elif digit == 2:
            value2 = value2 * 10 + 7
        
        print (value)

    def eight_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 8

        elif digit == 2:
            value2 = value2 * 10 + 8

        print (value)

    def nine_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 9

        elif digit == 2:
            value2 = value2 * 10 + 9

        print (value)

    def zero_():
        """In all number def's"""
        
        global value, value2

        if digit == 1:
            value = value * 10 + 0

        elif digit == 2:
            value2 = value2 * 10 + 0

        print (value)

    def plus_():
        global digit, operation

        operation = "sum"
        digit += 1

        print (digit)
        
    def minus_():
        global digit, operation

        operation = "minus"
        digit += 1

        print (digit)
        
    def divide_():
        global digit, operation

        operation = "divide"
        digit += 1

        print (digit)
        
    def ExactDivide():
        global digit, operation

        operation = "Edivide"
        digit += 1

        print (digit)
        
    def multi_():
        global digit, operation

        operation = "multi"
        digit += 1

        print (digit)

    def equal_():
        global total, digit

        digit = 1
        
        if operation == "sum":
            total = value + value2
            
        elif operation == "minus":
            total = value - value2
            
        elif operation == "divide":
            total = value / value2
            
        elif operation == "Edevide":
            total = value // value2
            
        elif operation == "multi":
            total = value * value2

        print(total)
        
    #numbers

    one = Button(screen, text=' 1 ', fg='black', bg='orange',
                    command=one_, height=4, width=4)

    two = Button(screen, text=' 2 ', fg='black', bg='orange',
                    command=two_, height=4, width=4)

    three = Button(screen, text=" 3 ", fg="black", bg="orange",
                   command=three_, height=4, width=4)
    
    four = Button(screen, text=" 4 ", fg="black", bg="orange",
                   command=four_, height=4, width=4)
    
    five = Button(screen, text=" 5 ", fg="black", bg="orange",
                   command=five_, height=4, width=4)
    
    six = Button(screen, text=' 6 ', fg='black', bg='orange',
                    command=six_, height=4, width=4)

    seven = Button(screen, text=' 7 ', fg='black', bg='orange',
                    command=seven_, height=4, width=4)

    eight = Button(screen, text=" 8 ", fg="black", bg="orange",
                   command=eight_, height=4, width=4)
    
    nine = Button(screen, text=" 9 ", fg="black", bg="orange",
                   command=nine_, height=4, width=4)
    
    zero = Button(screen, text=" 0 ", fg="black", bg="orange",
                   command=zero_, height=4, width=4)

    #operatons, equal & dot

    plus = Button(screen, text=' + ', fg='black', bg='orange',
                    command=plus_, height=4, width=4)
    
    minus = Button(screen, text=' - ', fg='black', bg='orange',
                    command=minus_, height=4, width=4)

    divide = Button(screen, text=' / ', fg='black', bg='orange',
                    command=divide_, height=4, width=4)
    
    Edivide = Button(screen, text=' // ', fg='black', bg='orange',
                    command=divide_, height=4, width=4)
    
    multi = Button(screen, text=' * ', fg='black', bg='orange',
                    command=multi_, height=4, width=4)

    equal = Button(screen, text=' = ', fg='black', bg='orange',
                    command=equal_, height=4, width=4)
    
    """percent = Button(screen, text=' % ', fg='black', bg='orange',
                    command=percent_, height=4, width=4)
    
    dot = Button(screen, text=' . ', fg='black', bg='orange',
                    command=dot_, height=4, width=4)
    
    clear = Button(screen, text=' C ', fg='black', bg='orange',
                    command=clear_, height=4, width=4)
    
    pm = Button(screen, text=' +/- ', fg='black', bg='orange',
                    command=pm_, height=4, width=4)"""

    one.grid(row=1, column=0)
    two.grid(row=1, column=1)
    three.grid(row=1, column=2)
    four.grid(row=2, column=0)
    five.grid(row=2, column=1)

    six.grid(row=2, column=2)
    seven.grid(row=3, column=0)
    eight.grid(row=3, column=1)
    nine.grid(row=3, column=2)
    zero.grid(row=4, column=0)

    plus.grid(row=1, column=5)
    minus.grid(row=2, column=5)
    divide.grid(row=3, column=5)
    Edivide.grid(row=4, column=5)
    multi.grid(row=5, column=5)
    equal.grid(row=6, column=5)
    
    screen.bind("<Escape>", close)

    screen.mainloop()
    
    break

quit()
