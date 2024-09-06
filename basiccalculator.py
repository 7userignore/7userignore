from tkinter import *
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")	
def clear():
    global expression
    expression = ""
    equation.set("")	
top = Tk()
top.configure(background="light green")
top.title("Simple Calculator")
top.geometry("500x500")
equation = StringVar()
expression_field = Entry(top, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)		
button1 = Button(top, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=1, width=7)
button1.grid(row=10, column=0)
button2 = Button(top, text=' 2 ', fg='black', bg='red',command=lambda: press(2), height=1, width=7)
button2.grid(row=10, column=1)
button3 = Button(top, text=' 3 ', fg='black', bg='red',command=lambda: press(3), height=1, width=7)
button3.grid(row=10, column=2)
button4 = Button(top, text=' 4 ', fg='black', bg='red',command=lambda: press(4), height=1, width=7)
button4.grid(row=12, column=0)
button5 = Button(top, text=' 5 ', fg='black', bg='red',command=lambda: press(5), height=1, width=7)
button5.grid(row=12, column=1)
button6 = Button(top, text=' 6 ', fg='black', bg='red',command=lambda: press(6), height=1, width=7)
button6.grid(row=12, column=2)
button7 = Button(top, text=' 7 ', fg='black', bg='red',command=lambda: press(7), height=1, width=7)
button7.grid(row=14, column=0)
button8 = Button(top, text=' 8 ', fg='black', bg='red',command=lambda: press(8), height=1, width=7)
button8.grid(row=14, column=1)
button9 = Button(top, text=' 9 ', fg='black', bg='red',command=lambda: press(9), height=1, width=7)
button9.grid(row=14, column=2)
button0 = Button(top, text=' 0 ', fg='black', bg='red',command=lambda: press(0), height=1, width=7)
button0.grid(row=16, column=0)
plus = Button(top, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=1, width=7)
plus.grid(row=10, column=3)
minus = Button(top, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=1, width=7)
minus.grid(row=12, column=3)
multiply = Button(top, text=' * ', fg='black', bg='red',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=14, column=3)
divide = Button(top, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=1, width=7)
divide.grid(row=16, column=3)
equal = Button(top, text=' = ', fg='black', bg='red',command=equalpress, height=1, width=7)
equal.grid(row=16, column=2)
clear = Button(top, text='Clear', fg='black', bg='red',command=clear, height=1, width=7) # type: ignore
clear.grid(row=16, column='1')
Decimal= Button(top, text='.', fg='black', bg='red',command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=18, column=0)
top.mainloop()
