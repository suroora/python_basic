from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x800")
root.config(bg="#F0E68C")
label1 = Label(root, text="QR CODE GENERATOR ", width=20, bg="#F0E68C", font=("Times New Roman", "20", "bold italic"))
label1.place(x=90, y=53)


def QR_code():
    link_add = name_entry.get()
    link = link_entry.get()
    fil_name = link_add + ".png"
    abc = pyqrcode.create(link)
    abc.png(fil_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(fil_name))
    image_label = Label(image=image)
    image_label.image = image
    can.create_window(350, 280, window=image_label)
    image_label.place(x=60, y=350)


canvas = Canvas(root, width=467, height=555, )
canvas.place(x=10, y=120)

name_label = Label(root, text=" Name of the Link : ", font=("Helvetica", "12", "bold italic"))
canvas.create_window(100, 50, window=name_label)
name_entry = Entry(root, bd=3)
canvas.create_window(310, 50, window=name_entry, width=260)
link_label = Label(root, text=" Link Address : ", font=("Helvetica", "12", "bold italic"))
canvas.create_window(80, 120, window=link_label)
link_entry = Entry(root, bd=3)
canvas.create_window(310, 120, window=link_entry, width=260)
but = Button(root, text="QR Code", width=25, command=QR_code, bd=5)
canvas.create_window(250, 200, window=but)

can = Canvas(root, width=370, height=300)
can.place(x=50, y=370)

root.mainloop()
