# me do the funi 

```py
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

ping = b'\x1b'
while True:
    try:
        try:
            recved = cs.recv(4096)
            
            if recved[0] == 27:
                print("probs a ping to server",recved[1:100])
                
            print("client",recved[:100])
            s.send(recved)
        except socket.timeout:
            pass
        try:
            recved = s.recv(4096)
            print("server",recved[:100])

            cs.send(recved)
        except socket.timeout:
            pass
    except KeyboardInterrupt:
        s.close()
        cs.close()
        break
```
so basically i wrote a localhost transmission proxy to monitor minecraft packets between server and client.


this should be pretty ez 