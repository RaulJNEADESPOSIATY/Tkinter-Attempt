
import tkinter as tk
from tkinter import *
import webbrowser


root = tk.Tk()

name = tk.Label(text="Web Design App", foreground="black", background="red")
boarder = tk.Canvas(width=900,height=800)


def music():
    webbrowser.open_new(r"https://open.spotify.com")
def shop():
    webbrowser.open_new(r"https://www.amazon.co.uk")


wideget = tk.Button(text="spotify", command=music, width=25)
wid2 = tk.Button(text="amazon", command=shop,width=25)
# img = PhotoImage(file="/Users/raul/Desktop/nebula.jpeg")
# label1 = Label(image = img).pack()


wid2.pack()
wideget.pack()



boarder.pack()
name.pack()
root.mainloop()