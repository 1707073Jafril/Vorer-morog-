#Importing important libraries

from tkinter import  *
import time
import datetime
import winsound as tune

#Alarm function is called for set up condition for alarming
def alarm(alarm_time):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now()
        now = time_now.strftime("%H:%M:%S")
        print("Present time is : ",now)
        print("Alarm time is : ", alarm_time)
        if now == alarm_time:
            print("Dear Sir! please wake up!")
            tune.PlaySound("sound.wav",tune.SND_ASYNC)
            break

#This fuction will receive input from user and handle alarm(alarm_time) function
def alarming():
    alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    #print("Alarm time is : ",alarm_time)
    alarm(alarm_time)

#following code is for GUI using Tkinter!

AlarmClock = Tk()
AlarmClock.title("vorer morog")
AlarmClock.geometry("400x200")
format_of_time = Label(AlarmClock,text="Please enter your time",bg="purple").place(x=100 , y=150)
addTime = Label(AlarmClock,text = "Hour  Min   Sec",font=60).place(x = 110)
setAlarm =Label(AlarmClock,text="Set Alarm Time!").place(x=0,y=30)
hour = StringVar()
min = StringVar()
sec = StringVar()
hourTime= Entry(AlarmClock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(AlarmClock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(AlarmClock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
submit = Button(AlarmClock,text = "Set Alarm",fg="red",width = 10,command =alarming).place(x =110,y=70)

AlarmClock.mainloop()
