def hello(name="World"):
    """
    Retourne un message de salutation personnalisé.
    
    :param name: Nom de la personne à saluer.
    """
    return f"Hello, {name} !"

if __name__ == "__main__":
    print(hello())

def get_country_from_ip(ip):
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