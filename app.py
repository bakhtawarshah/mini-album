from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('400x200')
root.title('Mini Album')

img1 = ImageTk.PhotoImage(Image.open("images/1.png"))
showImg = Label(image=img1)
showImg.grid(row=0, column=0)

root.mainloop()