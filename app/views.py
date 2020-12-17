from app import app
from flask import render_template
import tkinter as tk
from tkinter import filedialog

def open_file():
    #放入要讀取照片的位置
    root = tk.Tk()
    root.withdraw()
    image_url = filedialog.askopenfilename()  
    root.destroy()
    return image_url

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/', methods=['POST']) 
def open_file1():
    msg = open_file()
    return render_template('public/index.html',message=msg, image_url=msg)
