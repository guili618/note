from flask import Flask,redirect,url_for,abort,make_response,json,jsonify,request,session
import click



app = Flask(__name__)
app.secret_key = 'agasgderhdga4354356ygyg45'
#app.run(debug=True)

@app.route('/')
@app.route('/greet')
@app.route('/greet/<name>')
def index(name="world"):
    return "<h1>Hello,%s</h1>" % name



@app.cli.command()
def hello():
    click.echo("hello world")



@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d </p>' % (2018 - year)


@app.route('/register')
def register():
    return redirect(url_for('index'))


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea.'

@app.route('/foo')
def foo():
    response = make_response('hello world!')
    response.mimetype = 'text/plain'
    return response

@app.route('/bar')
def bar():
    data = {
        'name':"lilei",
        'age':"10"
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response

@app.route('/json')
def json():
    return jsonify(name='hanmeimei',age='18')



@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name',name)
    return response


@app.route('/')
@app.route('/test')
def test():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','human')
    return "<h1>Hello,%s</h1>" % name





@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('index'))



@app.route('/')
@app.route('/admin')
def admin():
    name = request.cookies.get('name')
    response = "<h1>Hello,%s</h1>" % name
    if name is None:
        name = request.cookies.get('name','human')
    if 'logged_in' in session:
        response += 'Authenticated'
    else:
        response += 'Not Authenticated'
    return response
