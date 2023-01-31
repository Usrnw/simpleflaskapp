from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def showhome():
    print("shw hme");
    return render_template("hmepg.html");

@app.route('/ajx', methods=['GET','POST'])
def ajx():
    print("res fun");
    if request.method== "POST":
        print("post");
        #cont= request.json;
        return "ihj";
    return render_template("ajx.html");
    
app.run()

