from redis import Redis
import time
import pickle

redis = Redis(host='redis', port=6379)

def process(x):
 print('Processing {}...')
 for k, v in x.items():
  print('Key: {} | Value: {}'.format(k, str(v)))
  redis.lpush('results', pickle.dumps([k, v]))
  time.sleep(1)
 print('...done!')

if __name__ == '__main__':
 print('Starting item processor...')
 while True:
  time.sleep(1)
  item = redis.rpop('my_list')
  if item:
   item = pickle.loads(item)
   process(item)
   
  
