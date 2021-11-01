import requests


base_url = "http://127.0.0.1:5000/employee"

r = requests.get(base_url+"/takuma")
print(r.text)

r = requests.post(base_url, data={"name": "takuma"})
print(r.text)

r = requests.put(base_url, data={"name": "takuma", "new_name": "tomori"})
print(r.text)

r = requests.delete(base_url, data={"name": "tomori"})
print(r.text)
