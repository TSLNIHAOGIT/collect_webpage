from flask import Flask, request, jsonify
app = Flask(__name__)

''''
是一种服务端与客户端的形式；服务端发起服务，客户去访问（以特定的链接加参数才可以）


'''

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print (content['mytext'])
#     return jsonify({"uuid":uuid})


#服务端获取客户端发来的json数据
@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json(silent=True,force=True)
    print('content',content) # Do your processing
    #response must be a string\tupe\ and so on.
    return jsonify(content)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)