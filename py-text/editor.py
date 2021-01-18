from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

filename = ''
main = Tk()

main.title("py-text")
main_scrollbar = Scrollbar(main)
main_scrollbar.pack(side=RIGHT, fill=Y)
main.minsize(height=200,width=200)

py_text= tk.Text(main)

def save_file():

    path_file = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not path_file:
        return
    with open(path_file, "w") as out_the_goddamn_file:
        txt = py_text.get(1.0, tk.END)
        out_the_goddamn_file.write(txt)

save_btn = tk.Button(main, text = 'save it ', command = lambda : save_file())
save_btn.pack(side = TOP, pady = 20,padx = 50)


py_text.pack()
main.mainloop()