import parser
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x400")
root.config(bg="pink")
display = Entry(root, bd=3, font=("bold", 25))
display.place(x=75, y=80, height=70)
# GET THE USER INPUT AND PLACE IT IN THE TEXT FIELD

i = 0


def vari(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0,END)


def back():
    undo=display.get()
    if len(undo):
        new_str=undo[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"0")


def get_operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def Equal():
    all_str=display.get()
    try:
        a=parser.expr(all_str).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")



# ADDING BUTTON TO THE CALCULATOR
but1 = Button(root, text=" 1 ", width=10 , command=lambda : vari(1))
but1.place(x=100, y=170)
but1 = Button(root, text=" 2 ", width=10, command=lambda : vari(2))
but1.place(x=180, y=170)
but1 = Button(root, text=" 3 ", width=10, command=lambda : vari(3))
but1.place(x=260, y=170)
but1 = Button(root, text=" AC", width=10, command=lambda :clear_all())
but1.place(x=340, y=170)
but1 = Button(root, text=" 4 ", width=10, command=lambda : vari(4))
but1.place(x=100, y=197)
but1 = Button(root, text=" 5 ", width=10, command=lambda : vari(5))
but1.place(x=180, y=197)
but1 = Button(root, text=" 6 ", width=10, command=lambda : vari(6))
but1.place(x=260, y=197)
but1 = Button(root, text=" - ", width=10, command=lambda :get_operation("-"))
but1.place(x=340, y=197)
but1 = Button(root, text=" 7 ", width=10, command=lambda : vari(7))
but1.place(x=100, y=224)
but1 = Button(root, text=" 8 ", width=10, command=lambda : vari(8))
but1.place(x=180, y=224)
but1 = Button(root, text=" 9 ", width=10, command=lambda : vari(9))
but1.place(x=260, y=224)
but1 = Button(root, text=" x ", width=10, command=lambda :get_operation("*"))
but1.place(x=340, y=224)
but1 = Button(root, text=" x! ", width=10, command=lambda :get_operation("x!"))
but1.place(x=100, y=251)
but1 = Button(root, text=" 0 ", width=10, command=lambda : vari(0))
but1.place(x=180, y=251)
but1 = Button(root, text=" . ", width=10, command=lambda : vari("."))
but1.place(x=260, y=251)
but1 = Button(root, text=" / ", width=10, command=lambda :get_operation("/"))
but1.place(x=340, y=251)
but1 = Button(root, text=" ( ",width=10, command=lambda : vari("("))
but1.place(x=100, y=278)
but1 = Button(root, text=" ) ", width=10, command=lambda : vari(")"))
but1.place(x=180, y=278)
but1 = Button(root, text=" % ", width=10, command=lambda :get_operation("%"))
but1.place(x=260, y=278)
but1 = Button(root, text=" PI ", width=10, command=lambda :get_operation("3.14"))
but1.place(x=180, y=305)
but1 = Button(root, text=" ^2 ", width=10, command=lambda :get_operation("**2"))
but1.place(x=260, y=305)
but1 = Button(root, text=" + ", width=10, pady=15, command=lambda :get_operation("+"))
but1.place(x=340, y=278)
but1 = Button(root, text=" = ", width=10, padx=41, command=lambda :Equal())
but1.place(x=180, y=332)
but1 = Button(root, text=" BACK", width=10,command=lambda :back())
but1.place(x=340, y=332)
but1 = Button(root, text=" EXP ", width=10 , pady=15, command=lambda :get_operation("**"))
but1.place(x=100, y=305)
# creating ToolBar

status = Label(root, text="Created by Suroora ", bd=2, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
