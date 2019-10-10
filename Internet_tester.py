import socket
import winsound
import time

while True:
    try:
        socket.create_connection(("www.google.com",80))
        print('*_*')
        winsound.Beep(5000,300)
        time.sleep(0.3)
    except:
        pass
