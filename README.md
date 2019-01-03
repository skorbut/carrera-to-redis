# serial-to-redis
Read Serial Connection events of a carrera digital slot car track and post events to Redis using python rq

It's an endless loop requesting information from a carrera control unit connected via USB, serial port given by ENV Variable SERIAL_PORT and adding to the redis queue identified by ENV Variable REDIS_QUEUE.

## Setup

clone the repository
```
git clone git@github.com:skorbut/serial-to-redis.git
```
change into directory and initialize virtual env
```
cd serial-to-redis/
python3 -m venv venv
. venv/bin/activate
```
install requirements
```
pip install -r requirements.txt
```

