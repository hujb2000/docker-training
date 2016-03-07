from flash import Flash
from redis import Redis
import os

app = Flash(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'Hello World! I have beennseen %s times. ' % redis.get('hits')

if __name__ =="__main__":
	app.run(host='0.0.0.0',debug=True)
