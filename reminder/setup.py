from cx_Freeze import setup, Executable
  
setup(name = "Reminder by Arjun" ,
      version = "0.1" ,
      description = "this is python code for a simple reminder application for windows using python the libraries used are tkinter for gui,win10toast for notification and winsound for notification beep sound" ,
      executables = [Executable("reminder.py")])