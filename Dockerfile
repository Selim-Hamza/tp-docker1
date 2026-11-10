# 1. Image de base légère (le système d'exploitation avec Python préinstallé)
FROM python:3.10-slim

# 2. Définition du répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copie des fichiers locaux vers le conteneur
COPY app.py .

# 4. Installation de la dépendance Flask
RUN pip install flask

# 5. Commande d'exécution au démarrage du conteneur
CMD ["python", "app.py"]