from tkinter import *
root = Tk()
welcomeText = Label(root, text="Hi")
welcomeText.grid(row=0, column=0)
saveButton = Button(root, text="Save")
saveButton.grid(row=1, column=0)
root.mainloop()
