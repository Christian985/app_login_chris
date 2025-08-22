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

def get_usuarios(token):
    try:
        url = f"{base_url}/usuarios"
        response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        return response.json()
    except Exception as e:
        print(e)
        return {
            "Error": f"{e}",
        }

def post_usuarios(email, senha, nome, papel, token):
    try:
        url = f"{base_url}/usuarios"
        dados = {
            "email": email,
            "senha": senha,
            "nome": nome,
            "papel": papel,
        }
        response = requests.post(url, json=dados, headers={"Authorization": f"Bearer {token}"})
        return response.json()
    except Exception as e:
        print(e)
        return {
            "Error": f"{e}",
        }