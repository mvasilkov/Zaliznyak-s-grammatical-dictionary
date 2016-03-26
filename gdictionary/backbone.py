#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from glob import glob
from os.path import join
import os
from io import BytesIO
import rusgrab
import uuid
from werkzeug import secure_filename
from ast import literal_eval
import json

app = Flask(__name__)
app.secret_key = 'zaliznyak'
UPLOAD_FOLDER = "static"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kira")
def kira():
    return render_template("kira.html")

@app.route("/nadin")
def nadin():
    return render_template("nadin.html")

@app.route("/ilya")
def ilya():
    return render_template("ilya.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html",  query="", result="")

@app.route("/prediction/form", methods=['GET', 'POST'])
def form_analyze():
    PATH_TO_DIC = os.path.abspath('examples.json') #insert path to examples.json here
    dic = json.loads(open(PATH_TO_DIC, encoding='utf8').read())
    query = request.values.get("message", "")
    result = rusgrab.main(query)
    if result == 1:
        flash("No more than 50 words!")
        return redirect(url_for('prediction'))
    result = result[1:]
    result = [item.strip().split(",") for item in result]
    result = [[item[0], " ".join(item[1:])] for item in result]
    exp = []
    for item in result:
        gram = item[-1]
        g = ' '.join(list(reversed(gram.replace("о", "").split())))
        if g in dic:
            exp.append(dic[g])
        else:
            exp.append("Not a noun")
    return render_template("prediction.html", query=query, result=result, popup=exp)

##def form_analyze():
##    query = request.values.get("message", "")
##    result = rusgrab.main(query)
##    result = result[1:]
##    return render_template("prediction.html",  query=query, result=result)

@app.route("/prediction/file", methods=['GET', 'POST'])
def file_analyze():
    if request.method == 'POST':
        errors = []
        infile = request.files['file']
        infile.seek(0, os.SEEK_END)
        file_length = infile.tell()
        infile.seek(0)
        if file_length > 20 * 1024 * 1024 + 1:
            errors.append("Filesize should be under 20Mb!")
        filename = secure_filename(infile.filename)
        if '.' in filename and filename.rsplit('.', 1)[1] in ["txt"]:
            pass
        else:
            errors.append("File should have the .txt extension!")
        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for('prediction'))
        try:
            query = infile.read().decode('utf-8')
        except UnicodeDecodeError:
            try:
                query = infile.read().decode('cp1251')
            except UnicodeDecodeError:
                flash("Encoding should be UTF-8 or Win-1251!")
                return redirect(url_for('prediction'))
        result = rusgrab.main(query)
        filename = str(uuid.uuid4())
        with open(join(UPLOAD_FOLDER, filename), 'wb') as out:
            out.write("".join(result).encode('utf8'))
    return render_template("prediction.html",  filename=filename)

@app.route("/feedback/send/<result>", methods=['GET', 'POST'])
def send(result):
    result = literal_eval(result)
    src=[]
    for value in request.values:
        with open("feedback.csv", 'a+', encoding='utf8') as out:
            out.write(','.join([",".join(result[int(value)]), 
                str(request.values.get(value, ''))]) + '\n')
##    for value in request.values:
##        with open("feedback.csv", 'a+', encoding='utf8') as out:
##            out.write(','.join([result[int(value)].strip(), 
##                request.values.get(value, '')]) + '\n')
    return "Thank you for your feedback!"

@app.route("/feedback/<result>")
def feedback(result):
    return render_template("feedback.html", result=literal_eval(result))

if __name__ == "__main__":
    app.run(debug=True)
