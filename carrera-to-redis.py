import settings
import serial
import os
import sys
import time
import json
import redis
from carreralib import ControlUnit
import rq

serial_port = os.getenv('SERIAL_PORT')
queue_name = os.getenv('REDIS_QUEUE')

if not serial_port:
  print('SERIAL_PORT is not defined')
  sys.exit(1)

if not queue_name:
  print('REDIS_QUEUE is not defined')
  sys.exit(1)

while True:
  try:
    cu = ControlUnit(serial_port)
    break
  except serial.serialutil.SerialException:
    print("control unit not connected")
    time.sleep(5)
print("control unit connected")

queue = rq.Queue(queue_name, connection=redis.StrictRedis())
print("Connected to redis queue")

while (True):
  status_or_timer = cu.request
  event_data = json.dumps(status_or_timer)
  event_name = type(status_or_timer).__name__
  queue.enqueue("app.tasks.%s" % event_name, event_data)
  time.sleep(0.01)
