from tkinter import *
import time

string = '1234567890-=qwertyuiop[]\ asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'

dis_time = None


def keyboard(event):
    global dis_time

    def delete():
        if dis_time <= time.time():
            text.delete(1.0, END)

    dis_time = time.time() + 5
    if event.char and event.char in string:
        print(event.char)
        text.after(5000, delete)


window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.config(bg="lightgrey")
window.title("Disappearing Text")

label = Label(window, text="Most Dangerous Writing App", font=('arial', 25, "bold"), bg="lightgray")
label.pack()

text = Text(window, height=10, bg="lightgrey", font=('arial', 20))
text.config(highlightcolor='black', highlightbackground='black')
text.bind('<Key>', keyboard)
text.focus()
text.pack(pady=200)

window.mainloop()
