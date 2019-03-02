from flask import Flask
from flask import jsonify
from flask import request
import requests
import json

app = Flask(__name__)

coin_dict = {
    "比特币": "btcbtc",
    "以太坊": "ethbtc",
    "莱特币": "ltcbtc",
    "EOS": "eosbtc"
}

# Pull crypto prices from web
wci_url = ("https://www.worldcoinindex.com/apiservice/ticker?"
           "key=SDG0iXcdsHXmXUhhEvYHYhTwhF2Wj8"
           "&label={}&fiat=usd")

# @app.route('/')
# def hello_world():
#     # return jsonify(fulfillmentText='Hello from Flask!')
#
#     coin_name='比特币'
#     price='100'
#     fiat_unit='美元'
#     success_response = "{}的价格是{:.2f}{}".format(coin_name, float(price), fiat_unit)
#
#     # dic = {'fulfillmentText':success_response}
#     # print('hh',jsonify(dic))
#     # # return jsonify(dic)
#     # return jsonify(fulfillmentText='Hello from Flask!')
#     t = {
#         'a': 1,
#         'b': 2,
#         'c': [3, 4, 5]
#     }
#     return json.dumps(t)


@app.route('/')
def hello_world():
    coin_name='比特币'
    price='100'
    fiat_unit="美元"
    # return jsonify(fulfillmentText='Hello from dialogflow Flask!')
    success_response = "{}的价格我通过网上查询是是{:.2f}{}".format(coin_name, float(price), fiat_unit)
    # success_response=success_response.encode('utf8').decode('utf8')
    # print('success_response',success_response)
    dic = {'fulfillmentText':success_response}
    return jsonify(dic) #返回序列化的dict
    # return str(dic)       #字符串化的dict


##有错，但是在dialogflow上却是可以的



@app.route('/get_price', methods=['GET', 'POST'])

# @app.route('/', methods=['GET', 'POST'])
def get_price():

    #服务器端获取客户端的请求（post/get），以及传递过滤的json参数
    json = request.get_json(silent=True, force=True,)
    print('myjson',json)

    # coin_name = json["queryResult"]["parameters"]["coin_name"]
    # # default_response = json["queryResult"]["fulfillmentText"]
    # # print('coin_name',coin_name)
    #
    # coin_code = coin_dict[coin_name]
    #
    # #另一个请求获取数据
    # r = requests.get(wci_url.format(coin_code))
    # price = r.json()["Markets"][0]["Price"]
    # fiat_unit = "美元"
    # # success_response = "{}的价格是{:.2f}{}".format(coin_name, float(price), fiat_unit)

    success_response='我爱你'
    dic = {'fulfillmentText':success_response} #服务器端没有返回时，dialogflow才会用静态的rensponse
    return jsonify(dic) #返回给客户端显示的数据
if __name__=='__main__':
    app.debug = False
    app.run(host='0.0.0.0',port=5000)    #这样用来监听所有的ip，团队调试用
#     https://3cb2cfe0.ngrok.io与http://0.0.0.0:5000/ 等价，外网也可以访问因为作了内网穿透
#
#
# myjson ={
#          'responseId': 'fa419530-b69b-4de4-aaa7-fec9ea0eef59',
#          'queryResult': {'queryText': '比特币现在多少钱',
#                          'parameters': {},
#                          'allRequiredParamsPresent': True,
#                          'fulfillmentText': '$coin_name的价格现在是100万，你想要去买么？',
#                          'fulfillmentMessages': [{'text': {'text': ['不要问我$coin_name的价格，你要去买么？']}}],
#                          'outputContexts': [{'name': 'projects/cryptoassistant-be67b/agent/sessions/c221b23c-d693-b7a0-aa3a-2812a5653b21/contexts/ask_price-followup',
#                                              'lifespanCount': 2,
#                                              'parameters': {'coin_name': 'EOS', 'coin_name2.original': '', 'coin_name3': '比特币', 'coin_name.original': '', 'coin_name2': '以太坊', 'coin_name3.original': ''}}],
#                          'intent': {'name': 'projects/cryptoassistant-be67b/agent/intents/dd7a6439-b18b-4a35-9ddb-ddcf53acab70', 'displayName': 'ask_price'},
#                          'intentDetectionConfidence': 0.65, 'languageCode': 'zh-cn'},
#          'originalDetectIntentRequest': {'payload': {}},
#          'session': 'projects/cryptoassistant-be67b/agent/sessions/c221b23c-d693-b7a0-aa3a-2812a5653b21'}
#
#
