from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})


def gen_segitiga(numb):
    
    numb = str(numb)
    
    segitiga = []
    
    for i in range(len(numb)):
        
        # ambil digit awal
        digit = numb[i]+'0'
        
        #tambahkan 0 sejumlah i
        kosong = '0'* i
        
        segitiga.append(digit + kosong)
        
    return segitiga


def is_prime(numb):
    if numb <= 1:
        return False
    for i in range(2, int(numb**0.5) + 1):
        if numb % i == 0:
            return False
    return True



@app.route('/api/generate_segitia', methods=['POST'])
def generate_segitiga():
    data = request.json
    number = data.get('number')

    
    segitiga = gen_segitiga(number)
    
    return jsonify({'result':segitiga})
    
    

@app.route('/api/generate_bilangan_ganji', methods=['POST'])
def generate_bilangan_ganjil():
    # get data input form 
    data = request.json
    number = int(data.get('number'))
    
    app.logger.info(number)
    

    nomer_ganjils = [ i for i in range(1, number) if i % 2 != 0 ]
    return jsonify({'result': nomer_ganjils})


@app.route('/api/generate_prima', methods=['POST'])
def generate_prima():
    data = request.json
    number = int(data.get('number'))
    
    # find bilangan prima
    
    prima_numbers = [i for i in range(2, number + 1) if is_prime(i)]
    return jsonify({'result':prima_numbers})
    








if __name__== '__main__':
    app.run(debug=True)