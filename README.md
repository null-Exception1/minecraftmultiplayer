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

# Client 
##### Rotation packet

Eg.
`0b 0016 c7ff6904 bf6c0811 01`
| packet length | packet type | yaw | pitch | extras |
| ------ | ------ | ------ | ------ | ------ | 
| 0b | 0016 | c7ff6904 | bf6c0811 | 01 | 

- `yaw` (IEEE 754 float)
- `pitch` (IEEE 754 float)

##### Position packet

Eg. 
`1b 0014 4050a1f624125cff 4051800000000000 c040e19c28a94569 01`

| packet length | packet type | x coord | y coord | z coord | extras |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 1b | 0014 | 4050a1f624125cff | 4051800000000000 | c040e19c28a94569 | 01 |

- `x` (IEEE 754 double)

- `y` (IEEE 754 double)

- `z` (IEEE 754 double)

##### Position + Rotation packet

Eg. 
`23 0015 40204eab2feef243 4053800000000000 c0596a896c563537 c3d73926 41cea6bd01`
| packet length | packet type | x coord | y coord | z coord | yaw | pitch | extras |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1b | 0014 | 4050a1f624125cff | 4051800000000000 | c040e19c28a94569 | c3d73926 | 41cea6bd | 01 |

- `x` (IEEE 754 double)

- `y` (IEEE 754 double)

- `z` (IEEE 754 double)

- `yaw` (IEEE 754 float)

- `pitch` (IEEE 754 float)

##### Player hits something (or nothing)
Eg. 
`03002f00` - fixed packet (doesn't change)
| packet length | packet type | end | 
| - | - | - |
| 03 | 002f | 00 | 

##### Player started sprinting

##### Player ends sprinting