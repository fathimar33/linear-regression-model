import flask
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
@app.route("/home",methods=["get"])
def fathi():
    return render_template("index.html")
@app.route("/handle_data",methods=["post"])
def handle_data():
    stu_name=request.form.get("stuname")
    en_score=float(request.form.get("score"))
    with open("C:\\Users\\mjavi\\Desktop\\python\\linearregression2\\linear.pkl","rb")as linearfile:
        ld=pickle.load(linearfile)
    un_score=ld.predict([[en_score]])[0][0]
    return render_template("final.html",un_score=un_score,stu_name=stu_name)
app.run(port="8090")