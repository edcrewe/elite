import json
from flask import Flask
from jinja2 import Template
app = Flask(__name__)

@app.route("/")
def hello():
    with open('templates/home.j2.py') as tmpl:
        template = Template(tmpl.read())
    with open('templates/runs.json') as fh:
        runs = json.loads(fh.read())
    return template.render(runs=runs)
