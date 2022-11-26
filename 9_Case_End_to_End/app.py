# Função do Flask e Request
from flask import Flask, request
from datetime import datetime

# Instancia do aplicativo
Aplicativo = Flask(__name__)

# Carregar o modelo
import joblib
Modelo = joblib.load('Modelo_Linear_v100.pkl')


# Rotas
@Aplicativo.route('/API/<Score>', methods=['GET'])
def Pagina_api( Score ):
    
    # Entrada
    entrada = datetime.now()
    
    Inpute_para_modelo = Score
    # Previsao
    try:
        Previsao = Modelo.predict( [[ float(Inpute_para_modelo) ]] )
        
        # Término
        saida = datetime.now()
        
        Dicionario ={
            'Parametro_cliente' : str(Inpute_para_modelo),
            'Risco_credito': str( round( Previsao[0], 2)),
            'Data_entrada': str(entrada),
            'Data_saida':str(saida),
            'Tempo_processamento': str(saida - entrada)
        }

        return Dicionario
    except:
        return f'Muitas requisições'

@Aplicativo.route('/')
def Pagina_Inicial():
    return 'Rota inicial sem uso, vá para /API'

# Lingando o Aplicativo
if __name__ == '__main__':
    Aplicativo.run( debug=True )
