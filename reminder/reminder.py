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
  ws = Tk()
  ws.title("simple reminder")
  ws.geometry('600x500')
  ws['bg'] = '#ffbf00'
  
  def printValue():
   content = user_input.get()
   min = time_reminder.get()
   min_int = float(min)
   dura = dura_beep.get()
   dura_int = int(dura)
   Label(ws, text=f'{content}, Registered!', pady=20, bg='#ffbf00').pack()
   Label(ws, text=f'{min}, Registered!', pady=20, bg='#ffbf00').pack()
   Label(ws, text=f'{dura}, Registered!', pady=20, bg='#ffbf00').pack()
   timer(content,min_int*60,dura_int*1000)


  Label(ws, text="what should you be reminded about").pack()
  user_input = Entry(ws)
  user_input.pack(pady=30)
  Label(ws, text="in how many minuts").pack()
  time_reminder = Entry(ws)
  time_reminder.pack(pady=30)
  Label(ws, text="duration of beep").pack()
  dura_beep = Entry(ws)
  dura_beep.pack(pady=30)

  Button( 
    ws,
    text="create reminder", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

  ws.mainloop()
  
