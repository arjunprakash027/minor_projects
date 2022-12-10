import winsound
from tkinter import *
from win10toast import ToastNotifier
import six
import appdirs
import packaging.requirements

def timer(reminder,times,dur):
    notify = ToastNotifier()
    notify.show_toast("Reminder by Arjun",f"""reminder in {times/60} mins""",duration=times)
    notify.show_toast(f"Reminder by Arjun",reminder,duration=1)
    winsound.Beep(2400,dur)

if __name__=="__main__":
  user_input  = str(input("what do you wanna be reminded about:"))
  time_reminder = float(input("in how many minuts:"))
  dura = int(input("duration of beep:"))
  timer(user_input,time_reminder*60,dura*1000)
 