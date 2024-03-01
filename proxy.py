import socket
import binascii
d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
d.bind(("localhost",25565))
d.listen()

cs, addr = d.accept()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('barbel.aternos.host')
s.connect((ip,50853))
#
s.settimeout(0.2)
cs.settimeout(0.2)

ping = b'\x1b'
while True:
    try:
        try:
            recved = cs.recv(4096)
            length = recved[0]
            if length == 27:
                #print("probs a ping to server",recved[1:100])
                pass
            if length == 11:
                print("rot",binascii.hexlify(recved))
            s.send(recved)
        except socket.timeout:
            pass
        try:
            recved = s.recv(4096)
            #print("server",recved[:100])

            cs.send(recved)
        except socket.timeout:
            pass
    except KeyboardInterrupt:
        s.close()
        cs.close()
        break
