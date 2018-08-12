import json
from flask import Flask, request
from jinja2 import Template
app = Flask(__name__)

@app.route("/")
def hello():
    with open('templates/home.html.j2') as tmpl:
        template = Template(tmpl.read())
    with open('templates/runs.json') as fh:
        runs = json.loads(fh.read())
    return template.render(runs=runs)

@app.route("/add")
def add():
    with open('templates/add.html.j2') as tmpl:
        template = Template(tmpl.read())
    return template.render()        

@app.route('/runpost', methods=['POST'])
def runpost():
    if request.form:
        with open('templates/runs.json') as fh:
            runs = json.loads(fh.read())
        run = {}
        run['datetime'] = request.form['date'] + ':' + request.form['time'] + '00'
        for key in request.form:
            if key not in ('date', 'time'):
                run[key] = int(request.form[key])
        runs.append(run)
        with open('templates/runs.json', 'w') as fh:        
            fh.write(json.dumps(runs))
    return hello()
