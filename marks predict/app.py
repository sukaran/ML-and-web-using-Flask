from flask import Flask, render_template, request, redirect
from sklearn.externals import joblib
#module name
app = Flask(__name__)
m = joblib.load("model.pkl")

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
	if request.method =='POST':
		hours = float(request.form['hours'][0][0])

		marks = str(m.predict([[hours]]))
	return render_template("index.html",your_marks = marks)


    
if(__name__)=='__main__':
	app.run(debug=True)
 

 #enctype="multipart/form-data"  <input type="text" name="no2" placeholder="Enter second  number">