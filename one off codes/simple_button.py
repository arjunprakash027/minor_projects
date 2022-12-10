import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'YOU ARE USELESS!!', fg='green', font=('helvetica', 30, 'bold'))
    canvas1.create_window(200, 200, window=label1)
    
button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(450, 450, window=button1)

root.mainloop()