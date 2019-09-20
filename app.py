from flask import Flask, request, escape

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

def fun(a):
  i = 10
  return i + a

if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=5006)
    
