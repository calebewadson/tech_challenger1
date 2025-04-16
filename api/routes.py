from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from scraping.producao import get_producao_data
from scraping.processamento import get_processamento_data
from scraping.comercializacao import get_comercializacao_data
from scraping.exportacao import get_exportacao_data
from scraping.importacao import get_importacao_data

auth = HTTPBasicAuth()

users = {"admin": "admin"}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

def register_routes(app):
    @app.route('/')
    def home():
        return jsonify({"msg": "API Viti Brasil"}), 200
    
    @app.route('/producao')
    @auth.login_required
    def producao():
        df = get_producao_data()
        return df.to_json(orient='records', force_ascii = False)
    
    @app.route('/processamento')
    @auth.login_required
    def processamento():
        df = get_processamento_data()
        return df.to_json(orient='records', force_ascii = False)
    

    @app.route('/comercializacao')
    @auth.login_required
    def comercializacao():
        df = get_comercializacao_data()
        return df.to_json(orient='records', force_ascii = False)
    

    @app.route('/exportacao')
    @auth.login_required
    def exportacao():
        df = get_exportacao_data()
        return df.to_json(orient='records', force_ascii = False)
    

    @app.route('/importacao')
    @auth.login_required
    def importacao():
        df = get_importacao_data()
        return df.to_json(orient='records', force_ascii = False)