import tkinter as tk
from tkinter.constants import END

window = tk.Tk()


border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}


for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.RIGHT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.RIGHT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT)

frames = tk.Frame(master=window, relief = tk.RAISED,borderwidth=3)
frames.grid(row=3,column=4,padx=5,pady=5)

greet = tk.Label(master=frames,text="hello",
foreground="white",
background="black",
width=20,
height=20)

but = tk.Button(master=frame,text="clickme",
foreground="white",
background="black",
width=20,
height=20)

entry =tk.Entry(master=frame,bg="white")

entry.insert(0,"arjun")
entry.insert(0,"rao") 
name = entry.get()
print(name)

text_box = tk.Text(master=frame)
txt = text_box.get("1.0",tk.END)
print(txt)




greet.place(x=20,y=5)

but.pack()

entry.pack()

text_box.pack()




window.mainloop()



