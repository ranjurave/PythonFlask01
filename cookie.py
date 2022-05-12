from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    session = requests.Session()
    #name = request.cookies.get("userID")
    #return f"<h1>welcome {name} </h1>"
    print(session)
    return 'name'

if __name__=='__main__':
    app.run(debug = True)