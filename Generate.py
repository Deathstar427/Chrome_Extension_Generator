import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

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

    def cpy(self, source):
        destination = os.path.dirname(os.path.abspath(__file__)) + '/' + os.path.basename(source)

        shutil.copyfile(source, destination)
        return os.path.basename(source)

    def Window(self):
        lab_name = ttk.Label(text="Extension name")
        lab_name.pack(fill=tk.X, padx=5, pady=5)
        self.ent_name = ttk.Entry(self.root)
        self.ent_name.pack(fill=tk.X, padx=5, pady=5)

        lab_ver = ttk.Label(text="App version")
        lab_ver.pack(fill=tk.X, padx=5, pady=5)
        self.ent_ver = ttk.Entry(self.root)
        self.ent_ver.pack(fill=tk.X, padx=5, pady=5)

        lab_ver = ttk.Label(text="Manifest version : 2 (default)")
        lab_ver.pack(fill=tk.X, padx=5, pady=5)

        lab_html = ttk.Label(text="Default html file name (without .html)")
        lab_html.pack(fill=tk.X, padx=5, pady=5)
        self.ent_html = ttk.Entry(self.root)
        self.ent_html.pack(fill=tk.X, padx=5, pady=5)

        Final_butt = ttk.Button(self.root, text ="Select icon" , command=self.Selected_File)
        Final_butt.pack(fill=tk.X, padx=5, pady=5)

        Final_butt = ttk.Button(self.root, text ="SUBMIT" , command=self.get_value)
        Final_butt.pack(fill=tk.X, padx=5, pady=5)

    def Create(self, APP_NAME, APP_VERSION, MANIFEST_VERSION, DEFAULT_POPUP):
        default_manifest = {
            "name": APP_NAME,
            "version": APP_VERSION,
            "manifest_version": MANIFEST_VERSION,
            "browser_action":{
                "default_popup": f"{DEFAULT_POPUP}.html",
                "default_icon": self.cpy(self.selected_file)
            },
            "permissions":["activeTab"]
        }

        with open(f"{DEFAULT_POPUP}.html", "w") as f:
            f.write(self.default_code)

        with open("manifest.json", "w") as f:
            json.dump(default_manifest, f)

        with open("HOW_TO_ADD_EXTENSION.txt", 'w') as f:
            f.write(self.READ_ME)

    def get_value(self):
        APP_NAME = self.ent_name.get()
        APP_VERSION = self.ent_ver.get()
        MANIFEST_VERSION = 2
        DEFAULT_POPUP = self.ent_html.get()

        print(APP_NAME, APP_VERSION, MANIFEST_VERSION, DEFAULT_POPUP)
        self.Create(APP_NAME, APP_VERSION, MANIFEST_VERSION, DEFAULT_POPUP)
        self.root.destroy()

    


root = tk.Tk()
Extension(root)
root.mainloop()