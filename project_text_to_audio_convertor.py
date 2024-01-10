from tkinter import *
import pyttsx3
engine=pyttsx3.init()
win=Tk()
win.title("Text_To_Audio_Converter")
win.configure(bg="red")
win.geometry("500x250")

#fuction
def speak():
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()

#Label frame
lf=LabelFrame(win,text="Text to Speech",font=35,bd=7,bg="blue")
lf.pack(fill="both",expand="yes",padx=15,pady=15)
Label(lf,text="Text",font=35,padx=25).pack(side=LEFT)
#entry--user enter his/her text
text=StringVar()
Entry(lf,width=35,bd=10,textvariable=text).pack(side=LEFT,padx=30)

#button
Button(lf,text="Speech",font=35,command=speak).pack(side=LEFT)
mainloop()

