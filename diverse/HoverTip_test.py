#Hover test tip
import tkinter as tk
from idlelib.tooltip import Hovertip

    
app = tk.Tk()
myBtn = tk.Button(app,text='?')
myBtn.pack(pady=30)
myLb = tk.Label(app, text="xxx", fg="blue")
myLb.pack()
myTip = Hovertip(myBtn,'This is \na multiline tooltip.')
myTipl = Hovertip(myLb, "text here")
app.mainloop()