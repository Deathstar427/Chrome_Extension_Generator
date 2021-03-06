import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
from PIL import Image

class Extension:
    def __init__(self, root):
        self.READ_ME = """How to add generated extension in google chrome?
        -> Open settings
        -> Click on extension tab
        -> Turn on developer mode
        -> Click on 'load unpacked'
        -> Select the folder containing your extension
        -> Your extension is added to chrome"""

        self.default_code = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            Your extension is ready.    
        </body>
        </html>"""
        self.root = root
        self.root.title("Extension Generator")
        self.root.geometry("500x500")
        self.Window()

    def Selected_File(self):
        self.selected_file = filedialog.askopenfilename(initialdir='C://', title='Select a icon file', filetypes = (("Text files", "*.png*"),))
        self.lab_selected_file.config(text=f" Selected icon: {self.selected_file}")        

    def Resize_img(self):
        im = Image.open(self.selected_file)
        resized_im_16 = im.resize((16, 16))
        resized_im_48 = im.resize((48,48))
        resized_im_16.save(f'./{self.APP_NAME}/16x16.png')
        resized_im_48.save(f'./{self.APP_NAME}/48x48.png')

    def cpy(self, source):
        destination = os.path.dirname(os.path.abspath(__file__)) + f'/{self.APP_NAME}/' + '128x128.png'

        shutil.copyfile(source, destination)
        return os.path.basename(source)

    def Window(self):
        lab_head = ttk.Label(text="Extension Properties", font=("Arial 20 bold"))
        lab_head.pack(fill=tk.X, padx=5, pady=5)

        canvas=Canvas(self.root, width=500, height=10)
        canvas.pack()
        canvas.create_line(5,5,350,5, fill="black", width=5)

        lab_name = ttk.Label(text="Extension name")
        lab_name.pack(fill=tk.X, padx=15, pady=5)
        self.ent_name = ttk.Entry(self.root)
        self.ent_name.pack(fill=tk.X, padx=15, pady=5)

        lab_ver = ttk.Label(text="App version")
        lab_ver.pack(fill=tk.X, padx=15, pady=5)
        self.ent_ver = ttk.Entry(self.root)
        self.ent_ver.pack(fill=tk.X, padx=15, pady=5)

        lab_ver = ttk.Label(text="Manifest version : 2 (default)")
        lab_ver.pack(fill=tk.X, padx=15, pady=5)

        lab_html = ttk.Label(text="Default html file name (without .html)")
        lab_html.pack(fill=tk.X, padx=15, pady=5)
        self.ent_html = ttk.Entry(self.root)
        self.ent_html.pack(fill=tk.X, padx=15, pady=5)

        lab_head = ttk.Label(text="Icon Properties", font=("Arial 20 bold"))
        lab_head.pack(fill=tk.X, padx=5, pady=5)

        canvas=Canvas(self.root, width=500, height=10)
        canvas.pack()
        canvas.create_line(5,5,350,5, fill="black", width=5)

        Final_butt = ttk.Button(self.root, text ="Select icon" , command=self.Selected_File)
        Final_butt.pack(fill=tk.X, padx=5, pady=5)

        self.lab_selected_file = ttk.Label(text="icon path: ")
        self.lab_selected_file.pack(fill=tk.X, padx=5, pady=5)

        Final_butt = ttk.Button(self.root, text ="SUBMIT" , command=self.get_value)
        Final_butt.pack(fill=tk.X, padx=5, pady=5)

    def Create(self):
        
        os.mkdir(self.APP_NAME)
        default_manifest = {
            "name": self.APP_NAME,
            "version": self.APP_VERSION,
            "self.MANIFEST_VERSION": self.MANIFEST_VERSION,
            "browser_action":{
                "self.DEFAULT_POPUP": f"{self.DEFAULT_POPUP}.html",
                "default_icon": self.cpy(self.selected_file)
            },
            "icons":{
                "128":"128x128.png",
                "48":"48x48.png",
                "16":"16x16.png"
            },
            "permissions":["activeTab"]
        }

        self.Resize_img()
        
        with open(f"./{self.APP_NAME}/{self.DEFAULT_POPUP}.html", "w") as f:
            f.write(self.default_code)

        with open(f"./{self.APP_NAME}/manifest.json", "w") as f:
            json.dump(default_manifest, f)

        with open(f"./{self.APP_NAME}/HOW_TO_ADD_EXTENSION.txt", 'w') as f:
            f.write(self.READ_ME)
        

    def get_value(self):
        self.APP_NAME = self.ent_name.get()
        self.APP_VERSION = self.ent_ver.get()
        self.MANIFEST_VERSION = 2
        self.DEFAULT_POPUP = self.ent_html.get()

        print(self.APP_NAME, self.APP_VERSION, self.MANIFEST_VERSION, self.DEFAULT_POPUP)
        self.Create()
        self.root.destroy()

root = tk.Tk()
App = Extension(root)
root.mainloop()