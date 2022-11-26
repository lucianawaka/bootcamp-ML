# Função do Flask e Request
from flask import Flask, request
from datetime import datetime

# Instancia do aplicativo
Aplicativo = Flask(__name__)

# Carregar o modelo
import joblib
Modelo = joblib.load('Modelo_Linear_v100.pkl')


# Rotas
@Aplicativo.route('/API/')
def Pagina_api():
    return 'Pagina está on! Lulu está On! Bora caminhar!!!'

@Aplicativo.route('/')
def Pagina_Inicial():
    return 'Rota inicial vazia, vá para /API'

# Lingando o Aplicativo
if __name__ == '__main__':
    Aplicativo.run( debug=True )
