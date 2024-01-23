from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/alumnos')
def alumnos():
	titulo = "UTL!!!"
	nombres = ["Mario", "Juan", "Pedro", "Dario"]
	return render_template('alumnos.html', titulo=titulo, nombres=nombres)

@app.route('/maestros')
def maestros():
	return render_template('maestros.html')



@app.route('/hola')
def hola():
  	return "<h1>Saludos desde la pagina de hola</h1>"

@app.route('/saludo')
def saludo():
  	return "<h1>Saludos desde la pagina de Saludo</h1>"

@app.route('/nombre/<string:nombre>')
def nombre(nombre):
  	return f" <h1> Hola {nombre} </h1>"

@app.route('/numero/<int:n1>')
def edad(n1):
  	return f"numero {n1}"

@app.route('/numero/<int:n1>/<string:nombre>')
def edadNombre(n1,nombre):
  	return f"ID: {n1} Nombre: {nombre}"

@app.route('/numero/<float:n1>/<float:n2>')
def suma(n1,n2):
  	return f"suma: {n1+n2}"

@app.route('/default')
@app.route('/default/<string:d>')
def defecto(d="defecto"):
  	return f"valor por defecto: {d}"




if __name__ == '__main__':
	app.run(debug=True)