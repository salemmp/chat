from flask import Flask,render_template
from flask_socketio import SocketIO,emit,disconnect


app= Flask(__name__)
app.config['SECRET_KEY']='123'

sio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@sio.on('connect')
def event(json):
    print('alguien se ha conectado')
  


@sio.on('btn')
def event(json):
    texto=json['texto']
    usuario=json['usuario']
    print(f'{usuario} dice: {texto}')
    response=f'{usuario}: {texto}'

    
    sio.emit('servidor',response)
   

