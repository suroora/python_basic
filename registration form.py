from tkinter import *
from tkinter import Label

root = Tk()
root.title("Registration_Form")
root.geometry('500x800')
label1 = Label(root, text="Registration form", width=20, font=("Helvetica", "20", "bold italic underline"))
label1.place(x=90, y=53)

label2 = Label(root, text="Username : ", width=20, font=("bold", 15))
label2.place(x=50, y=150)

entry1 = Entry(root)
entry1.place(x=220,y=155)

label3 = Label(root, text="Mobil Number : ", width=20, font=("bold", 15))
label3.place(x=33, y=205)

entry2 = Entry(root)
entry2.place(x=220,y=210)


label4 = Label(root, text="E-mail : ", width=20, font=("bold", 15))
label4.place(x=65, y=260)

entry3 = Entry(root)
entry3.place(x=220,y=265)

label5 = Label(root, text="age : ", width=20, font =("bold", 15))
label5.place(x=74, y=315)
entry4 = Entry(root)
entry4.place(x=220,y=320)

label6= Label(root, text="Password : ", width=20, font=("bold", 15))
label6.place(x=48, y=370)
entry5 = Entry(root)
entry5.place(x=220,y=375)

label7 = Label(root, text="Conform Password : ", width=20, font=("bold", 15))
label7.place(x=7, y=425)
entry6 = Entry(root)
entry6.place(x=220,y=430)

button=Button(root,text="LOGIN",width=20)
button.place(x=50,y=500)
button1=Button(root,text="CANCEL",fg="red",width=20)
button1.place(x=300,y=502)
root.mainloop()
