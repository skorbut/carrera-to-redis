import os
import sys
import serial
import time
import json
import redis
from datetime import datetime

serial_port = os.environ.get('SERIAL_PORT')
if not serial_port:
  print('SERIAL_PORT is not defined')
  sys.exit(1)
redis_list = os.environ.get('REDIS_LIST') or 'track-events'


ser = serial.Serial(serial_port, 9600, timeout=0)
r = redis.StrictRedis()



while (True):
  if (ser.in_waiting>0):
    data_str = ser.read(ser.in_waiting).decode('ascii')
    event_string = json.dumps({'timestamp': datetime.now().isoformat(), 'payload': data_str})
    r.rpush(redis_list, event_string)
  time.sleep(0.01)
