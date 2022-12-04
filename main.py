from flask import Flask,render_template,redirect,url_for,request
import mysql.connector
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/course")
def service():
    return render_template("course.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/result",methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        database="test",
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        result=request.form.to_dict()
        name=result['name']
        phone=result['phone']
        email=result['email']
        text=result['text']
        mycursor.execute("insert into userdata (name,phone,email,text)values(%s,%s,%s,%s)",(name,phone,email,text))
        mydb.commit()
        mycursor.close()
        return "Success"
    return render_template("contact.html")
if __name__ == '__main__':
    app.run()