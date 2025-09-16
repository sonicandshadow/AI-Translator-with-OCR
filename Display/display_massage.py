import threading
import tkinter as tk
content = ""
area = (0,0,0,0)
label = tk.Label


def update_massage(con):
    global content
    content = con
    update_label()


def update_area(ar):
    global area
    area = ar


def update_label():
    global label
    global content
    global area
    label.config(text=content)
    label.config(wraplength=abs(area[0] - area[2]))
    label.place(x=area[0],y=area[1])


def show_massage():
    global content
    global  area
    global  label
    root = tk.Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    root.attributes('-topmost', 'true')
    # root.attributes('-alpha', 1)
    root.attributes('-transparentcolor', 'black')
    root.config(bg='black')
    # lable = tk.Label(root,fg='white', text=content, font=('宋体',20), wraplength=300, bg='black').place(x=area[0]-area[2],y=area[1]-area[3])
    # label = tk.Label(root,fg='white', text=content, font=('宋体',20), wraplength=abs(area[0]-area[2]), bg='black').place(x=area[0],y=area[1])
    label = tk.Label(root, fg='white', text=content, font=('宋体', 20), wraplength=abs(area[0] - area[2]), bg='black')
    label.place(x=area[0],y=area[1])
    # label.config(text="test")
    root.mainloop()

if __name__ == "__main__":
    show_massage(

    )