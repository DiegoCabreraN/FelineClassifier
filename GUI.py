import tkinter as tk
import Classifier
from tkinter import filedialog
from PIL import ImageTk, Image

class GUI:
    def __init__(self):
        self.filepath = ''
        self.root = tk.Tk()

        positionRight = int(self.root.winfo_screenwidth()/2 - self.root.winfo_reqwidth()/2)
        positionDown = int(self.root.winfo_screenheight()/2 - self.root.winfo_reqheight()/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.root.title('Feline Classifier')

        self.top_frame = tk.Frame(self.root)
        self.title_label = tk.Label(self.top_frame, text = "Welcome to my Feline Classifier!")
        self.title_label.config(font=("", 25))
        self.description_label = tk.Label(self.top_frame, text = "Please, upload an image in order to proceed.")
        self.description_label.config(font=("", 13))
        logo = ImageTk.PhotoImage(Image.open('./src/cat.jpeg'))
        self.image_label = tk.Label(self.top_frame, image=logo)

        self.top_frame.pack( padx = (10,10) )
        self.title_label.pack( pady = (10,5) )
        self.description_label.pack( pady = (0,10) )
        self.image_label.pack( pady = (0,10) )

        self.bottom_frame = tk.Frame(self.root)
        self.start_button = tk.Button(
            self.bottom_frame, 
            text ="Check Image", 
            command = self.checkImage, 
            width=30, 
            state=tk.DISABLED
        )
        self.upload_button = tk.Button(
            self.bottom_frame, 
            text ="Select Image", 
            command = self.selectFile, 
            width=30
        )


        self.bottom_frame.pack( pady = (0,10) )
        self.upload_button.pack( side = tk.LEFT )
        self.start_button.pack( side = tk.LEFT)

        self.root.mainloop()

    def selectFile(self):
        self.filepath = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (
                ("jpg files","*.jpg"),
                ("jpeg files","*.jpeg*"),
                ("png files","*.png*")
            )
        )
        self.start_button['state'] = tk.NORMAL

    def checkImage(self):
        self.description_label.pack_forget()
        detected = Classifier.Model(self.filepath)
        if type(detected) != tuple and detected:
            new_title = 'A {}{} cat was detected!'.format(detected[0].upper(),detected[1:])
            self.title_label.config(text = new_title)
        elif detected:
            new_title = 'A {}{} was detected!'.format(detected[0][0].upper(),detected[0][1:])
            self.title_label.config(text = new_title)
        else:
            new_title = 'No feline was detected!'
            self.title_label.config(text = new_title)

        logo = ImageTk.PhotoImage(Image.open(self.filepath).resize((300, 300), Image.ANTIALIAS))
        self.image_label.config(image = logo)
        self.image_label.image = logo
        self.upload_button.config(text = 'Select Another Image')
        self.start_button['state'] = tk.DISABLED


GUI()