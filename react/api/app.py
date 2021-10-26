from flask import Flask, request, render_template
from replit import db

app = Flask(__name__, template_folder='templates', static_folder='static')
    
@app.route('/messaging', methods=['POST', 'GET'])
def message():
    username = request.form['username']
    #if username in db:
    return render_template(
         'username-taken.html'
     )   


app.run('0.0.0.0', 8080)