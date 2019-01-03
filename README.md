# serial-to-redis
Read Serial Connection events of a carrera digital slot car track and post events to Redis using python rq

It's an endless loop requesting information from a carrera control unit connected via USB, serial port given by ENV Variable SERIAL_PORT and adding to the redis queue identified by ENV Variable REDIS_QUEUE.
