import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost",25565))
s.listen()

cs, addr = s.accept()

print(cs.recv(1024))

print(cs.send(b'\x03\x03\x80\x02'))

f = eval(open('servershit.txt','r').read())

for i in f:
    #print(i)
    cs.send(i)
    print(cs.recv(1024))