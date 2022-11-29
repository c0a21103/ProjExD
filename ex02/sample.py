import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn =event.widget
    txt = btn["text"]
    tkm.showinfo("tk",f"{txt}ボタンが押されました")

root = tk.Tk()
root.title("test")
root.geometry("500x200")
label = tk.Label(root,text="Label",font=("",20))
label.pack()
# button = tk.Button(root,text="押すな",command=button_click)
button = tk.Button(root,text="押すな")
button.bind("<1>",button_click)
button.pack()
entry = tk.Entry(width=30)
entry.insert(tk.END,"hoge")
entry.pack()