from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time

def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Wake up!!!")
            toast.show_toast("Wake up!!!",duration=1)
            playsound("")

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.geometry("270x220")
info = Label(root,text = "(24)Hour  Min   Sec").place(x = 40)
set_time = Label(root,text = "Set Time",relief = "solid",font=("Cambria",10,"bold")).place(x=50,y=50)


hour = StringVar()
min = StringVar()
sec = StringVar()


hour_E = Entry(root,textvariable = hour,bg = "blue",width = 10).place(x=50,y=30)
min_E = Entry(root,textvariable = min,bg = "pink",width = 10).place(x=100,y=30)
sec_E = Entry(root,textvariable = sec,bg = "grey",width = 10).place(x=150,y=30)

submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x =50,y=70)

root.mainloop()