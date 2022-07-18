from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
app = Flask(__name__)

@app.route("/" , methods=['GET',"POST"])
def add_numbers():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        result = float(num1) + float(num2)
        return render_template('result.html',add=result)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)