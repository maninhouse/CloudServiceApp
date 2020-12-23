from app import app
from flask import render_template
from flask import request
import tkinter as tk
from tkinter import filedialog
from . import visual_recognition as vr

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/', methods=['POST']) 
def open_file1():
    
    image_url = request.values.get('input_url')
    result = vr.visual_recognition(image_url = image_url)
    return render_template('public/index.html', msg=result)
