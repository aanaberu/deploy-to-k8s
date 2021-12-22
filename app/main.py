from flask import Flask
app = Flask(__name__)

#Normal nginx app display
#test123 pipeline
@app.route("/")
def hello():
    return "Hello this is K8 deployment demo using DAI Release and Deploy server 21"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
