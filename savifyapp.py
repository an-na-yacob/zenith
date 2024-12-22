import google.generativeai as genai
from flask import Flask, render_template, request

genai.configure(api_key="YOUR API KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/taskpage')
def taskpage():
    return render_template('taskpage.html')

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():
    target = ""
    expenses = ""
    generated_task = None
    if request.method == 'POST':
        target = request.form['target']
        expenses = request.form['expenses']
        # Generate content using Gemini API with a simplified prompt
        prompt = f"Generate a simple, single-sentence task to help achieve the goal of: '{target}' considering the expense: '{expenses}'"
        response = model.generate_content(prompt)
        generated_task = response.text.strip()
    return render_template('addtask.html', target=target, expenses=expenses, task=generated_task)
@app.route('/lastpage')
def lastpage():
    return render_template('lastpage.html')
if __name__ == '__main__':
    app.run(debug=True)
