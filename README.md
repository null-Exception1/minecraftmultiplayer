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

# client 
# `'0016'` - means rotation packet

the rotation is a bit weird though, but ill still explain it

the packet is 11 bytes long and looks something like this

`b'0b0016c7ff6904bf6c081101'`

`0b` 0016 c7ff6904 bf6c0811 01 (spaced for clarity)

`0b` is the packet length, 0016 is packet type (rotation)

`c7ff6904` - x rotation (IEEE 754 floating point)

`bf6c0811` - y rotation (IEEE 754 floating point)

# `'0014'` - means position packet

`1b 0014 4050a1f624125cff 4051800000000000 c040e19c28a94569 01`(spaced for clarity)

`1b` is packet length, `0014` is packet type (position).

`4050a1f624125cff` - x (IEEE 754 double)

`4051800000000000` - y (IEEE 754 double)

`c040e19c28a94569` - z (IEEE 754 double)

# `'0015'` - means position + rotation packet

`b'23001540204eab2feef2434053800000000000c0596a896c563537c3d7392641cea6bd01'`

`23 0015 40204eab2feef243 4053800000000000 c0596a896c563537 c3d73926 41cea6bd01` (spaced for clarity)

`23` - packet size

`0015` - packet type (pos + rot)


`40204eab2feef243 4053800000000000 c0596a896c563537` - x,y,z
`c3d73926 41cea6bd01` - yaw, pitch





