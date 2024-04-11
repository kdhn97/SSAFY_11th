import requests


response = requests.get('http://127.0.0.1:8000/api/v1/libraries/')

# json을 python 타입으로 변환
result = response.json()