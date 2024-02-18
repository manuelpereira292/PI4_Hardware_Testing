from adafruit_dht import DHT11
import board
from time import sleep

dht_device = DHT11(board.D3)

try:
    while True:
        try:
            temp_c = dht_device.temperature
            hu = dht_device.humidity
            print('(T:', temp_c, 'C) (H:', hu, '%)')
            sleep(5)
        except RuntimeError as err:
            print(err.args[0])

except KeyboardInterrupt:
    pass
