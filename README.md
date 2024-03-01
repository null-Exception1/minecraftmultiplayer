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


first thing im discovering is that packet lengths are specified at the beginning of a packet, very noice very interesting. looking at the minecraft wiki, i saw that the first byte always specifies the length of the total packet in the netcode.

the 2nd and 3rd bytes are kind of like an instructor on what the packet is supposed to be about

i see how this can be useful if you want to not get ddosed with the client sending huge huge amount of packets.

# '\x00\x16' - means rotation packet

the rotation is a bit weird though, but ill still explain it

the packet is 11 bytes long and looks something like this

b'0b0016c7ff6904bf6c081101' (hexdigested)

0b 0016 c7ff6904 bf6c0811 01

0b is the packet length, 0016 is packet type (rotation)

c7ff6904 - x rotation
bf6c0811 - y rotation 

there's a difference of 1440 for a turn of 180 degrees which is a bit too precise to be in a block game. 

here's the weirdest part: if i start turning clockwise over and over, you would assume the x rotation to reset when it hits 360, because 0 comes after 360 in degrees. but nope. it adds up all the extra turns along with the super precise 360 degrees it's already sending. this is highly redundant and i dont know how this can be useful at all, maybe if there's a lot of lag then you could make use of this, but still this is too much precision.

makes me want to overflow the x rotation with just turning over and over.

# '\x00\x14@' - means position packet




