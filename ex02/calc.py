import tkinter as tk
import tkinter.messagebox as tkm

r = c = 0

def button_click(event):
    btn =event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}ボタンが押されました")

root = tk.Tk()
root.title("tk")
root.geometry("300x500")
for i in range(9,-1,-1):
    button = tk.Button(root,text=f"{i}",width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

root.mainloop()