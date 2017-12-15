from flask import Flask, request, jsonify
from redis import Redis
import pickle

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET'])
def hello():
 count = redis.incr('hits')
 return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/my_list/', methods=['POST'])
def push_to_redis():
 data = request.json
 redis.lpush('my_list', pickle.dumps(data))
 return jsonify(data), 201

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)

