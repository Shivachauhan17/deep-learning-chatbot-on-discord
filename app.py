from flask import Flask,render_template,request
app=Flask(__name__)

import prediction_logic

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output',methods=['POST','GET'])
def output():
    if request.method == 'POST':
        sentence=request.form['question']
        p=prediction_logic.predict(str(sentence))
        return render_template('index.html',answer=p)

if __name__ == "__main__":
    app.run(port=5000,debug=True)