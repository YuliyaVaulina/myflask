import requests

#### создаем объявление

url = 'http://127.0.0.1:5000/advertisements'
json = {
        'title': 'Продам комод',
        'description': 'Старенький, но в хорошем состоянии',
        'date_created': '2022-05-01',
        'owner': 'Шапокляк'
        }
response = requests.post(url, json=json)
print(response.json())


#### получаем все объявления

# url = 'http://127.0.0.1:5000/advertisements'
# response = requests.get(url)
# print(response.json())


#### получаем объявление по идентификатору

# url = 'http://127.0.0.1:5000/advertisements/3'
# response = requests.get(url)
# print(response.json())


####  удаляем объявление по идентификатору

# url = 'http://127.0.0.1:5000/advertisements/1'
# response = requests.delete(url)
# print(response.json())

