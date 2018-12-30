# serial-to-redis
Read Serial Connection and Post Events to Redis

It's an endless loop reading from the serial port given by ENV Variable SERIAL_PORT and adding to the redis list identified by ENV Variable REDIS_LIST.
