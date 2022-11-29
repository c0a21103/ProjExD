import tkinter as tk

def button_click(event):
    btn =event.widget
    txt = btn["text"]
    inner = entry.get()
    if txt ==  "=":
        inner = inner.translate(str.maketrans({"÷":"/","×":"*"}))
        ans = eval(inner)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    elif txt == "+/-":
        if "-" in inner:
            res = inner.replace("-","")
        else:
            res = "-" + inner
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    elif txt == "%":
        pars = int(inner)
        pars = pars/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,pars)
    elif txt == "C":
        print(inner)
        d = len(inner)-1
        entry.delete(d,tk.END)
    elif txt == "AC":
        entry.delete(0,tk.END)
        entry.insert(tk.END,"0")
    else:
        if inner == "0" and txt == ".":
            pass
        elif inner == "0":
            entry.delete(0,tk.END)
            
        entry.insert(tk.END,txt)
        

root = tk.Tk()
root.title("tk")
root.geometry("376x580")
entry = tk.Entry(root,justify="right",width=20,font=("",20))
entry.insert(tk.END,"0")
entry.grid(row=0,column=0,columnspan=4,sticky=tk.EW)
r,c = 2,2
for num in range(9,-1,-1):
    if num != 0:
        button = tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
        button.bind("<1>",button_click)
        button.grid(row = r,column = c)
    else:
        button = tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
        button.bind("<1>",button_click)
        button.grid(row = r,column = 0)
    c -= 1
    if c == -1:
        r += 1
        c = 2

button = tk.Button(root,text=".",width=4,height=2,font=("",30))
button.bind("<1>",button_click)
button.grid(row = r,column = 1)
button = tk.Button(root,text="%",width=4,height=2,font=("",30))
button.bind("<1>",button_click)
button.grid(row = r,column = 2)

lst = ["C","AC","+/-"]
r,c = 1,0
for x in lst:
    button = tk.Button(root,text=x,width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    c += 1
    if c == -1:
        r += 1
        c = 2

entity = ["=","+","-","×","÷"]
r = 5
for ent in entity:
    button = tk.Button(root,text=ent,width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row = r,column = 4)
    r -= 1

root.mainloop()