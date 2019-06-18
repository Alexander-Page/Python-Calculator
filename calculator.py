from Tkinter import *

window = Tk()
window.geometry('456x370+200+200')
window.title("Calculator")

operands = []
numop = 0
global num1
global operator

def enter(event=None):
    global num1
    global operator
    num1 = int(num1)
    num2 = int(output.get('1.0', END))
    if operator is "add":
        result = num1 + num2
        print result, num1, num2
        output.delete('1.0', END)
        output.insert(END, result)
    elif operator is "sub":
        result = num1 - num2
        output.delete('1.0', END)
        output.insert(END, result)
    elif operator is "mult":
        result = num1 * num2
        output.delete('1.0', END)
        output.insert(END, result)
    elif operator is "div":
        result = num1 / num2
        output.delete('1.0', END)
        output.insert(END, result)
    #output.delete('1.0', END)


def clear(event=None):
    output.delete('1.0', END)


def func1(event=None):
    output.insert(END, "1")


def func2(event=None):
    output.insert(END, "2")


def func3(event=None):
    output.insert(END, "3")


def func4(event=None):
    output.insert(END, "4")


def func5(event=None):
    output.insert(END, "5")


def func6(event=None):
    output.insert(END, "6")


def func7(event=None):
    output.insert(END, "7")


def func8(event=None):
    output.insert(END, "8")


def func9(event=None):
    output.insert(END, "9")


def func0(event=None):
    output.insert(END, "0")

def add(event=None):
    global num1
    num1 = output.get('1.0', END)
    global operator
    operator = "add"
    output.delete('1.0', END)

def sub(event=None):
    num1 = output.get('1.0', END)
    operator = "sub"
    output.delete('1.0', END)

def mult(event=None):
    num1 = output.get('1.0', END)
    operator = "mult"
    output.delete('1.0', END)

def div(event=None):
    num1 = output.get('1.0', END)
    operator = "div"
    output.delete('1.0', END)


output = Text(window, height=5, width=57, wrap=WORD)
output.grid(row=0, column=0, columnspan=4, sticky=NW)

button1 = Button(window, text="1", width=15, height=4, command=func1)
button1.grid(row=1, column=0, sticky=NW)
window.bind('1', func1)

button2 = Button(window, text="2", width=15, height=4, command=func2)
button2.grid(row=1, column=1, sticky=NW)
window.bind('2', func2)

button3 = Button(window, text="3", width=15, height=4, command=func3)
button3.grid(row=1, column=2, sticky=NW)
window.bind('3', func3)

button4 = Button(window, text="4", width=15, height=4, command=func4)
button4.grid(row=2, column=0, sticky=NW)
window.bind('4', func4)

button5 = Button(window, text="5", width=15, height=4, command=func5)
button5.grid(row=2, column=1, sticky=NW)
window.bind('5', func5)

button6 = Button(window, text="6", width=15, height=4, command=func6)
button6.grid(row=2, column=2, sticky=NW)
window.bind('6', func6)

button7 = Button(window, text="7", width=15, height=4, command=func7)
button7.grid(row=3, column=0, sticky=NW)
window.bind('7', func7)

button8 = Button(window, text="8", width=15, height=4, command=func8)
button8.grid(row=3, column=1, sticky=NW)
window.bind('8', func8)

button9 = Button(window, text="9", width=15, height=4, command=func9)
button9.grid(row=3, column=2, sticky=NW)
window.bind('9', func9)

button0 = Button(window, text="0", width=15, height=4, command=func0)
button0.grid(row=4, column=1, sticky=NW)
window.bind('0', func0)

buttonenter = Button(window, text="Enter", width=15, height=4, command=enter)
buttonenter.grid(row=4, column=2, sticky=NW)
window.bind('<Return>', enter)

buttonclear = Button(window, text="Clear", width=15, height=4, command=clear)
buttonclear.grid(row=4, column=0, sticky=NW)
window.bind('<Delete>', clear)

buttonadd = Button(window, text="+", width=15, height=4, command=add)
buttonadd.grid(row=1, column=3, sticky=NW)
window.bind('+', add)

buttonsub = Button(window, text="-", width=15, height=4, command=sub)
buttonsub.grid(row=2, column=3, sticky=NW)
window.bind('-', sub)

buttonmult = Button(window, text="*", width=15, height=4, command=mult)
buttonmult.grid(row=3, column=3, sticky=NW)
window.bind('*', mult)

buttondiv = Button(window, text="/", width=15, height=4, command=div)
buttondiv.grid(row=4, column=3, sticky=NW)
window.bind('/', div)

window.mainloop()
