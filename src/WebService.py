#!/bin/python3

from flask import Flask, request
import controller
app = Flask(__name__)

@app.route('/')
def hello_class():
	return 'Hello, CDK class!'

@app.route('/saludo/<persona>')
def saludoDinamico(persona):
	return 'Hola %s, bienvenido!' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
	resp = num * num
	return 'Respuesta: %f' % resp

@app.route('/rlineal', methods=['POST'])
def preRLineal():
	if request.method == 'POST':
		data = request.get_json()
		print(data)
		vx = data['vx']
		vy = data['vy']
		x = data['x']
		return controller.getRLineal(vx,vy,x)
	else:
		return "not found"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)

