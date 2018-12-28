### Linux output输出到web
---
###
```py
import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        proc = subprocess.Popen(
            ['dmesg'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

app.run(debug=True, port=5000, host='127.0.0.1')
```
- 来源：https://stackoverflow.com/questions/15041620/how-to-continuously-display-python-output-in-a-webpage

- TODO 改成django，并且可以渲染模板

- https://stackoverflow.com/questions/15041620/how-to-continuously-display-python-output-in-a-webpage
```py

import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(100):
            time.sleep(1)
            yield '%s<br/>\n' % x
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('result.html')
    return flask.Response(tmpl.generate(result=inner()))

app.run(debug=True)

```

```html
{% extends "layout.html" %}
{% block body %}
<body>
  {% for line in result %}
    {{ line }}
  {% endfor %}
</body>
{% endblock %}


```


```py
from flask import Response, escape
from yourapp import app
from subprocess import Popen, PIPE, STDOUT

SENTINEL = '------------SPLIT----------HERE---------'
VALID_ACTIONS = ('what', 'ever')

def logview(logdata):
    """Render the template used for viewing logs."""
    # Probably a lot of other parameters here; this is simplified
    return render_template('logview.html', logdata=logdata)

def stream(first, generator, last):
    """Preprocess output prior to streaming."""
    yield first
    for line in generator:
        yield escape(line.decode('utf-8'))  # Don't let subproc break our HTML
    yield last

@app.route('/subprocess/<action>', methods=['POST'])
def perform_action(action):
    """Call subprocess and stream output directly to clients."""
    if action not in VALID_ACTIONS:
        abort(400)
    first, _, last = logview(SENTINEL).partition(SENTINEL)
    path = '/path/to/your/script.py'
    proc = Popen((path,), stdout=PIPE, stderr=STDOUT)
    generator = stream(first, iter(proc.stdout.readline, b''), last)
    return Response(generator, mimetype='text/html')

@app.route('/subprocess/<action>', methods=['GET'])
def show_log(action):
    """Show one full log."""
    if action not in VALID_ACTIONS:
        abort(400)
    path = '/path/to/your/logfile'
    with open(path, encoding='utf-8') as data:
        return logview(logdata=data.read())

```