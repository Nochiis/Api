from flask import Flask, jsonify, request

# TODO: CREAR UNA INSTANCIA DE LA APLICACIÓN FLASK
app = Flask(__name__)

#TODO: DATOS DE EJEMPLO PARA USUARIOS
usuarios = [{'id':1, 'nombre': 'John'},{'id':2, 'nombre': 'William'}, {'id':3, 'nombre': 'Juan'}]
    
# TODO: DEFINIR UNA RUTA PARA LA PÁGINA PRINCIPAL
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

#TODO: DEFINIR UNA RUTA PARA LA PÁGINA DE USUARIOS
@app.route('/usuarios')
def obtener_usuarios():
    #TODO: CONVERTIR LA LISTA EN UN JSON Y DEVOLVERLOS COMO RESPUESTA AL REQUEST
    return jsonify({'usuarios': usuarios})

#TODO: DEFINIR RUTA PARA OBTENER UN USUARIO POR ID
@app.route('/usuarios/<int:id_usuario>')
def obtener_usuario(id_usuario):
    #TODO: BUSCAR EL USUSARIO POR ID EN LA LISTA DE USUARIOS
    usuario = next((user for user in usuarios if user['id']==id_usuario),None)
   
    #TODO: VERIFICAR SI SE ENCUENTRA EL USUARIO Y DEVOLVERLO, DE LO CONTRARIO INDICAR QUE NO LO ENCUENTRA
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensaje':'Usuario no encontrado'}),404
    
#TODO: BUSCAR UN USUARIO POR NOMBRE
@app.route('/buscar')
def buscar_usuario():
    #TODO: ASIGNAMOS UN ARGUMENTO A NOMBRE PARA BUSCARLO POR LA URL
    nombre = request.args.get('nombre')
    usuarios_encontrado = [user for user in usuarios if nombre.lower() in user['nombre'].lower()]

    #TODO: VALIDAMOS SI ENCUENTRA EL USUARIO POR NOMBRE
    if usuarios_encontrado:
        return jsonify({'usuarios': usuarios_encontrado})
    else:
        return jsonify({'mensaje':'Usuario no encontrado'}),404
    
   
# TODO: INICIAR LA APLICACIÓN SI ESTE SCRIPT ES EJECUTADO DIRECTAMENTE
if __name__ == "__main__":
    # TODO: CONFIGURACIÓN PARA EJECUTAR LA APLICACIÓN EN MODO DEPURACIÓN
    app.run(debug=True)


