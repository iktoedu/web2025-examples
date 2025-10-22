from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    tpl_data = {}
    if request.method == 'POST':
        tpl_data['username'] = request.form['username']
        tpl_data['email'] = request.form['email']
    return render_template('form.html.j2', **tpl_data)
