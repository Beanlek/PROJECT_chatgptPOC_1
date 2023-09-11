from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open", command=open_file)
button.pack()
window.mainloop()