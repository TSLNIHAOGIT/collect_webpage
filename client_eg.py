import requests
res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"from client :lalala"})
# res = requests.post('http://localhost:5000/get_price', json=
# {
# "queryResult":
#     {"parameters":
#          {"coin_name":'比特币'}
#      }
#
# })

if res.ok:
    print('res.json()',res.json())