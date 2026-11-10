from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Le nom d'hôte 'mongo' fera référence au service défini dans docker-compose
client = MongoClient('mongodb://mongo:27017/')

@app.route('/')
def hello_world():
    try:
        # Test de la connexion à la base de données
        client.admin.command('ping')
        status = "Connexion à MongoDB réussie !"
    except Exception as e:
        status = f"Échec de connexion : {e}"
    
    return f"Hello, World depuis Flask et Docker ! <br><br> Statut BDD : {status}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)