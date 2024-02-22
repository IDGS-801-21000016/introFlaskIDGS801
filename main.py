from flask import Flask, render_template, request
from forms import UserForm
from flask import flash 
from flask import g
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.secret_key = 'DFGHJKLI67890'


@app.before_request
def before_request():
	g.nombre = "Jonarro"
	print("Antes de la peticion")

@app.after_request
def after_request(response):
	print("Despues de la peticion")
	response.headers['powered-by'] = 'Jonarro'
	return response
	

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
	# titulo = "UTL!!!"
	# nombres = ["Mario", "Juan", "Pedro", "Dario"]
	# return render_template('alumnos.html', titulo=titulo, nombres=nombres)
	usuario_form = UserForm(request.form)
	nombre = None
	p_apellido = None
	m_apellido = None
	edad = None
	email = None
	
	
	if request.method == 'POST' and usuario_form.validate():
		nombre = usuario_form.nombre.data
		m_apellido = usuario_form.a_materno.data
		p_apellido = usuario_form.a_paterno.data
		edad = usuario_form.edad.data
		email = usuario_form.email.data
	
		print(f"Nombre: {nombre} {p_apellido} {m_apellido} Edad: {edad} Email: {email}")

		msj_flash = f"Bienvenido {g.nombre}"
		flash(msj_flash)
	return render_template('alumnos.html', form=usuario_form, nombre=nombre, p_apellido=p_apellido , m_apellido=m_apellido, edad=edad, email=email if email else "Email")
												

@app.route('/maestros')
def maestros():
	return render_template('maestros.html', img = "a")


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
		

@app.errorhandler(404)
def error(error):
		return render_template('404.html', error = error), 404
   

    




if __name__ == '__main__':
	app.run(debug=True)