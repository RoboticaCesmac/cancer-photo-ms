from flask import Flask, request, jsonify
from PIL import Image
from os import listdir
from os.path import isdir
import numpy as np
from tensorflow import keras
# from keras import backend as K
import requests
import base64
import io
model = keras.models.load_model('modelo-treinado')

def select_image(filename):
    # load image from file
    if(filename.startswith('http')):
        image = Image.open(requests.get(filename, stream=True).raw) #ARQUIVO URL
    else:
        image = Image.open(io.BytesIO(base64.b64decode(str(filename)))) #ARQUIVO FISICO
    # convert to RGB, if needed
    image = image.convert('RGB')
    image = image.resize((150,150))
    # convert to array
    return np.asarray(image)

###########################################

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Bem vindo a API de Reconhecimento de imagens do Projeto de Mestrado do CESMAC!'

@app.route('/image', methods=["POST"])
def analyse():
    data = request.json
    image = data['image']

    image = select_image(image)
    image = np.array(list(image)) / 255.0  ## convertendo de lista para array

    #### Recupera o modelo treinado

    results = model(np.array([image]))
    result = results[0].numpy()    
    #K.clear_session() #Libera espaço na memoria

    print(result)
    response = {"value":0, "acc":0, "animal": ""}
    print('----------------------------------')
    print(result[0])
    print(result[1])
    if (result[0] > result[1]):
        response["value"] = "0"
        response["value_name"] = "Não possui câncer"
        response["acc"] = str(result[0])
    else:
        response["value"] = "1"
        response["value_name"] = "Pode ter câncer"
        response["acc"] = str(result[1])

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')