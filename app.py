from flask import Flask, jsonify, request
from flask_restful import reqparse
from DAO import DAO
import logging, json




logging.basicConfig(filename='desafioElo.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


app = Flask("desafioElo")


@app.route('/api/deploy', methods=['POST', 'GET'])
def deploy():
    if request.method == 'POST':
        data = request.json
        print(jsonify(data))
        DAO.insert_mysql(data)

        return jsonify(data)
    else:
        data = DAO.get_dadozs()

        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
