import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('pigfish.aternos.host')
s.connect((ip,50853))

s.send(b'\x10\x00\xfb\x05\tlocalhostc\xdd\x02\x1c\x00\tcheese312\x01X\x07fd\xb1\x0e6/\xa9\xf5\xd3q.-\x05V')

print(s.recv(1024))

s.send(b'2')

l = []
while True:
    d = s.recv(4096)
    print(d)
    if d == b'':
        break
    l.append(d)


print(l)
