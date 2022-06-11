from gtts import gTTS
import os
from tkinter import *
root=Tk()
root.title('Text to Speech Converter')
root.geometry('250x250')
root.config(bg='#87CEFA')


def text_speech():
    text=entry.get()
    output = gTTS(text=text, lang='en', slow=.75)
    output.save('output.mp3')
    os.system('start output.mp3')
label1=Label(root,text="Enter you text here :",bg='#87CEFA' ,font=('bold'' italic ',10))
label1.place(x=20,y=28)
entry=Entry(root,bd='6')
entry.place(x=20 ,y=50,width=210,height=40, )
but=Button(text="click here",command=text_speech,bd='4')
but.place(x=100,y=100)

root.mainloop()