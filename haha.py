from tkinter import *
import webbrowser

def open_link(event):
    # You can change this to any URL or function call
    webbrowser.open_new("https://www.example.com")

root = Tk()
root.title("Hyperlink Example")
root.geometry("300x200")

# Create a label that looks like a hyperlink
hyperlink = Label(root, text="Click here to visit Example.com", fg="blue", cursor="hand2")
hyperlink.pack(pady=20)

# Bind the label to the open_link function
hyperlink.bind("<Button-1>", open_link)

root.mainloop()
