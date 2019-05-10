from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index_project.html")

if __name__ == '__main__':
   app.run(debug=True,use_reloader=True)