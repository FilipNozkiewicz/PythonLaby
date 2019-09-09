import urllib.request , urllib.parse
import random
import time
import logging

print('Staarting client....')

data = 'Id:123:I am 123'
data = bytes(data.encode())

try:
    while True:
        try:
            response = urllib.request.urlopen('http://127.0.0.1:8095' , data).read()
            print(response)
        except:
            logging.warning('Connection Error')
        time.sleep(random.randint(1,4))
except KeyboardInterrupt:
    print('Client Stopped')