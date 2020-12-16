from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from app import views, admin_views
