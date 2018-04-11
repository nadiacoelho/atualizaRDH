import requests
import userSettings
import montaURL

endereco = montaURL.enderecoLogin

usuario = userSettings.usuario
senha = userSettings.senha

resp = requests.post(endereco, data = {'username': usuario , 'password': senha})
print(resp.status_code)