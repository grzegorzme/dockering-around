from flask import Flask, jsonify
from redis import Redis
import pickle


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
 count0 = redis.get('hits') 
 if count0:
  count0 = count0.decode('utf-8')
 else:
  count0 = 0
 count = redis.incr('hits2')
 return 'Hello World! I have been seen {} times and the other one has been seen {} times.\n'.format(count, count0)

@app.route('/my_list/', methods=['GET'])
def get_from_redis():
 data = redis.lrange('results', 0, -1)
 print(data)
 data = [pickle.loads(e) for e in data]
 return jsonify(data or {'error': 'no items found'})

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)

