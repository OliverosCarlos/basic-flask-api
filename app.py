from flask import Flask, render_template, request
import redis

app = Flask(__name__)

#REDIS CONNECTION
redis_cli = redis.Redis(
host='localhost',
port=6379,
charset="utf-8",
decode_responses=True
)

connection = redis_cli.ping()

if connection :
     print("Redis connected")
     redis_cli.setnx('counter',0)
else :
    print("Redis Unable to connect")

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        redis_cli.incr('counter')
        return "OK"
    
    if request.method == 'GET':
    
        data = {
            'count': redis_cli.get('counter'),
            'label': 'vez' if redis_cli.get('counter') == "1" else 'veces'
        }

        return render_template('home.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)