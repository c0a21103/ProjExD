import tkinter as tk
import random
import maze_maker


def key_down(event):
    global key
    key = event.keysym
    

def key_up(event):
    global key
    key = ""
    
def main_proc():
    global cx, cy, mx, my, tori1, tori2
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
        canvas.delete("kokaton")
        canvas.create_image(cx, cy, image=tori1, tag="kokaton")
    if key == "Right":
        mx += 1
        canvas.delete("kokaton")
        canvas.create_image(cx, cy, image=tori2, tag="kokaton")
        
    if key == "r":
        canvas.delete("kokaton")
        canvas.create_image(cx, cy, image=tori2, tag="kokaton")
    if key == "l":
        canvas.delete("kokaton")
        canvas.create_image(cx, cy, image=tori1, tag="kokaton")
        
    if maze_lst[mx][my] == 1:
        if key == "Up":
            my += 1
        if key == "Down": 
            my -= 1
        if key == "Left": 
            mx += 1
            canvas.delete("kokaton")
            canvas.create_image(cx, cy, image=tori1, tag="kokaton")
        if key == "Right":
            mx -= 1
            canvas.delete("kokaton")
            canvas.create_image(cx, cy, image=tori2, tag="kokaton")

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(300,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    maze_lst = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,maze_lst)
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori1 = tk.PhotoImage(file="ex03/fig/5.png")
    tori2 = tk.PhotoImage(file="ex03/fig/2.png")
    canvas.create_image(cx, cy, image=tori1, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()