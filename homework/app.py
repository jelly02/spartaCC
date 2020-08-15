from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello ubuntu and sparta!'

if __name__=='__main__':
    app.run('127.0.0.1',port=5000,debug=True)