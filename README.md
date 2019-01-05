# carrera-to-redis
Read Serial Connection events of a carrera digital slot car track and post events to Redis using python rq

It's an endless loop requesting information from a carrera control unit connected via USB, serial port given by ENV Variable SERIAL_PORT and adding to the redis queue identified by ENV Variable REDIS_QUEUE.

To connect a REDIS not running on the local machine or using a different port use the ENV Variable REDIS_URL to supply the Redis URL.

## Setup

clone the repository
```
git clone git@github.com:skorbut/carrera-to-redis.git
```
change into directory and initialize virtual env
```
cd carrera-to-redis/
python3 -m venv venv
. venv/bin/activate
```
install requirements
```
pip install -r requirements.txt
```

## Deployment to Raspberry Pi

Setup project as described above. Create a supervisor configuration defining the env variables to point to the correct serial port and redis queue.

```
[program:carrera-to-redis]
command=/home/deploy/carrera-to-redis/venv/bin/python carrera-to-redis.py
directory=/home/deploy/carrera-to-redis
user=deploy
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

