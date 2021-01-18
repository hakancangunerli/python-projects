import tkinter as tk
import time
from datetime import datetime, timezone
from tkinter import simpledialog
from pytz import timezone
import webbrowser

main = tk.Tk()
main.geometry("500x500")
main.title("timezone machine!")

canvas1 = tk.Canvas(main, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(main)
canvas1.create_window(200, 140, window=entry1)

def callback():
    webbrowser.open_new(r"https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568")
github_link = tk.Button(main, text="list of accepted timezones!", command=callback)


def getSquareRoot():
    def taym(USER_INP):
        data = timezone(str(USER_INP))
        what = datetime.now(data)
        formatted = what.strftime('%Y:%m:%d %H:%M:%S')
        return formatted
    inp = entry1.get()
    label1 = tk.Label(main, text=taym(inp.strip()))
    canvas1.create_window(200, 230, window=label1)

button1 = tk.Button(text='get time!', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

github_link.pack()
main.mainloop()


''''
# implementation without tk 
USER_INP = input("put in timezone: ")
data = timezone(str(USER_INP))
what = datetime.now(data)

formatted= what.strftime('%Y:%m:%d %H:%M:%S')

print(formatted)
'''