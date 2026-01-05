# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Empêcher Python de générer des fichiers .pyc et forcer l'affichage des logs en temps réel
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer les dépendances système nécessaires pour PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Exposer le port sur lequel FastAPI va tourner
EXPOSE 8000

# Commande pour lancer l'application avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]