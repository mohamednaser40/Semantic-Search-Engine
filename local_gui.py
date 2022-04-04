from tkinter import *
from app import *

if __name__ == '__main__':
    window = Tk()
    window.title("Semantic Search Engine")
    window.geometry('850x220')
    lbl = Label(window, height=11, text="No results yet")
    lbl.grid(row=10, column=5)
    txt = Entry(window, width=35)
    txt.grid(row=3, column=5)

    def clicked():
        res = main(txt.get())
        if res == 0:
            res = "[-] The data set is quite small I couldn't find anything, try fetching some more using the crawler."
        else:
            res = res.replace("$", "\n")
        lbl.configure(text=res)
    btn = Button(window, text="Search", command=clicked)
    btn.grid(row=3, column=6)
    footer = Label(window, text="[!] EELU - 2020")
    footer.grid(row=100, column=0)
    window.mainloop()