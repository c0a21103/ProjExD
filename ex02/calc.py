import tkinter as tk
import tkinter.messagebox as tkm

r = 1
c = 0

def button_click(event):
    btn =event.widget
    txt = btn["text"]
    if txt ==  "=":
        fml = entry.get()
        ans = eval(fml)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,txt)
    # tkm.showinfo(txt,f"{txt}ボタンが押されました")

root = tk.Tk()
root.title("tk")
root.geometry("300x500")
entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

for num in range(9,-1,-1):
    button = tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    c += 1
    if c == 3:
        r += 1
        c = 0
        
entity = ["+","="]
for ent in entity:
    button = tk.Button(root,text=ent,width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    c += 1
    if c == 3:
        r += 1
        c = 0

root.mainloop()