import subprocess
import sys

def install_requirements():
    """Installe les requirements nécessaires (ici requests) si non installés."""
    try:
        import requests
    except ImportError:
        print("La bibliothèque 'requests' n'est pas installée, installation en cours...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

install_requirements()  # Vérifie et installe les dépendances nécessaires

import requests

def get_country(ip):
    """
    Retourne le pays associé à une adresse IP en utilisant l'API ipinfo.io.
    :param ip: L'adresse IP à géolocaliser.
    :return: Le pays ou un message d'erreur si l'IP est invalide.
    """
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()
        return data.get("country", "Pays non trouvé")
    except Exception as e:
        return f"Erreur : {e}"
