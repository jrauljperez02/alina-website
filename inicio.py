from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/acercade')
def acercade():
    return render_template('acercade.html')
 
@app.route('/contacto')
def contacto ():
    return render_template('contacto.html')
 
@app.route('/servicios')
def servicios ():
    return render_template('servicios.html')
 
@app.route('/sistemas')
def sistemas ():
    return render_template('sistemas.html')
 
if __name__ == '__main__':
    app.run(debug=True)
