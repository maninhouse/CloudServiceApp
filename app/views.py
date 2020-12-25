from app import app
from flask import render_template
from flask import request
import tkinter as tk
from tkinter import filedialog
from . import visual_recognition as vr
from . import notify
import json

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/', methods=['POST']) 
def main_func():
    image_url = request.values.get('input_url')
    if (image_url == ""):
        return render_template('public/index.html', msg="請勿空白")
    a=request.values.get("select")
    result = vr.visual_recognition(image_url = image_url)
    jsonObject = json.loads(result)
    jsImage=jsonObject["images"][0]
    jsClassifier=jsImage["classifiers"][0]
    jsClass=jsClassifier["classes"]
    show = ''
    for i in range(len(jsClass)):
        jsResult = str(jsClass[i]["class"])
        if(jsResult.find(a)!=-1):
            show = "照片中有"+a
            break
        else : show = "照片中沒有"+a
    notify.notify(show, image_url)

    return render_template('public/index.html', msg=show,img=image_url)
