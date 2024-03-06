from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def generate_weekly(request):
    try:
        data = request.get_json()
        # Lógica para gerar o PDF usando os dados recebidos
        pdf_content = f"PDF Content for {data}"
        return jsonify({"statusCode": 200, "body": pdf_content})
    except Exception as e:
        print(f"Erro ao gerar o PDF: {e}")
        return jsonify({"statusCode": 500, "body": "Erro ao gerar o PDF"})

def home(request):
    try:
        return jsonify({"statusCode": 200, "body": "Serviço Python Next Automações"})
    except Exception as e:
        return jsonify({"statusCode": 500, "body": "Erro interno"})

# Define a rota / como a função de manipulação de eventos
@app.route('/generate/weekly', methods=['POST'])
def generate_weekly_route():
    return generate_weekly(request)

@app.route('/')
def home_route():
    return home(request)
