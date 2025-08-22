import requests

base_url = "http://10.135.235.34:5002"

def post_login(email, senha):
    try:
        url = f"{base_url}/login"
        dados = {
            "email": email,
            "senha": senha,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "Error": f"{e}",
        }

def get_usuarios():
    try:
        url = f"{base_url}/usuarios"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "Error": f"{e}",
        }

def post_usuarios(email, senha, nome, papel):
    try:
        url = f"{base_url}/usuarios"
        dados = {
            "email": email,
            "senha": senha,
            "nome": nome,
            "papel": papel,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "Error": f"{e}",
        }