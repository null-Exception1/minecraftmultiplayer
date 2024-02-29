import socket

d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

d.bind(("localhost",25565))
d.listen()

cs, addr = d.accept()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('luderick.aternos.host')
s.connect((ip,50853))

s.settimeout(1.0)
cs.settimeout(1.0)

while True:
    try:
        recved = cs.recv(4096)
        #print(recved)
        s.send(recved)
    except socket.timeout:
        pass
    try:
        recved = s.recv(4096)
        #print(recved)

        cs.send(recved)
    except socket.timeout:
        pass

