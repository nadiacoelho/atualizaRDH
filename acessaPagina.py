import requests

endereco = 'http://www.tidia-ae.usp.br/portal'
usuario = '8994265'
senha = '1753109462'

response = requests.post(endereco, data = {'eid': usuario , 'pw': senha})

print(response.status_code)