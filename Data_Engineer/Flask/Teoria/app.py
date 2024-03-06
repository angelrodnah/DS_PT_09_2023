from flask import Flask

app = Flask(__name__)

def index():
    return "Hello World!"

app.add_url_rule('/', 'index', index)
app.run(debug=True)

@app.route("/user/<name>")

def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/user/<name>/<int:index>")
def index(name, index):
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return name,index, mylist, mydict,mytuple

if __name__ == '__main__':
    app.run()