from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
# app.config.from_object('config')


@app.route('/')
def hello():
    return "hello"
