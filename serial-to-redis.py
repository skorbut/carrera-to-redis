import os
import serial
import time
import json
import redis
from datetime import datetime

ser = serial.Serial(os.environ.get('SERIAL_PORT'), 9600, timeout=0)
r = redis.StrictRedis()
redis_list = os.environ.get('REDIS_LIST') or 'track-events'


while (True):
  if (ser.in_waiting>0):
    data_str = ser.read(ser.in_waiting).decode('ascii')
    event_string = json.dumps({'timestamp': datetime.now().isoformat(), 'payload': data_str})
    r.rpush(redis_list, event_string)
  time.sleep(0.01)
