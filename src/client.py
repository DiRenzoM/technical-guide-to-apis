import requests

r = requests.get('http://localhost:5000/1')
#payload = {"data": "post_data", "id": 1}
#r = requests.post('http://localhost:5000', json=payload)

print(r.text)