from flask import Flask, render_template, request

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


@app.route('/calcular' , methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        return f"La multiplicacion de {n1} * {n2} = {n1*n2}"
    else:
        return """
    <form action="/calcular" method="POST">
		<label for="n1">Numero 1</label>
        <input type="text" name="n1" id="n1">
		<br>
		<label for="n2">Numero 2</label>
        <input type="text" name="n2" id="n2">
        <input type="submit" value="Enviar">
    </form>
        """
		
@app.route('/operasBas')
def operasBas():
  	return render_template('operasBas.html')

@app.route('/resultado' , methods=['GET', 'POST'])
def resultado():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        return f"La multiplicacion de {n1} * {n2} = {n1*n2}"
   

    




if __name__ == '__main__':
	app.run(debug=True)