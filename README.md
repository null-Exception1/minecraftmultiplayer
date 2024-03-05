# me do the funi 

this is a dissection of what happens in minecraft networking.

to try testing stuff myself, i wrote a localhost transmission proxy to monitor minecraft packets between server and client (proxy.py)

i've spaced different sections of the "example" packets for clarity, they aren't visible in actual packets.

this netcode protocol is for minecraft version 1.20.1, only works for online-mode as of now.

i will be releasing a sort of client module for controlling a minecraft client using python.

# Client 
---
### Rotation packet

Eg.
`0b 0016 c7ff6904 bf6c0811 01`
| packet length | packet type | yaw | pitch | extras |
| ------ | ------ | ------ | ------ | ------ | 
| 0b | 0016 | c7ff6904 | bf6c0811 | 01 | 

- `yaw` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) float
- `pitch` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) float

> Only triggered when rotation is done without movement.
> A server packet is recieved for correction every couple seconds.

---
### Position packet

Eg. 
`1b 0014 4050a1f624125cff 4051800000000000 c040e19c28a94569 01`

| packet length | packet type | x coord | y coord | z coord | extras |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 1b | 0014 | 4050a1f624125cff | 4051800000000000 | c040e19c28a94569 | 01 |

- `x` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

- `y` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

- `z` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

> This is only triggered when movement happens without rotation.
> A server packet is recieved for correction every couple seconds.
---
### Position + Rotation packet

Eg. 
`23 0015 40204eab2feef243 4053800000000000 c0596a896c563537 c3d73926 41cea6bd01`
| packet length | packet type | x coord | y coord | z coord | yaw | pitch | extras |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 23 | 0015 | 40204eab2feef243 | 4053800000000000 | c0596a896c563537 | c3d73926 | 41cea6bd | 01 |

- `x` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

- `y` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

- `z` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) double

- `yaw` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) float

- `pitch` is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) float

> This is only triggered when position happens with rotation.
> A server packet is recieved for correction every couple seconds.

---
### Player hits something (or nothing)

Eg. 
`03 002f 00`

| packet length | packet type | end | 
| - | - | - |
| 03 | 002f | 00 | 

> Note : The content of the packet does not change.

---
### Player started sprinting

Eg.
`06 001eea0f 0300`

| packet length | packet type | uuid | sprint/stop | 
| - | - | - | - |
| 06 | 001e | ea0f | 0300 | 


---
### Player ends sprinting

Eg.
`06 001eea0f 0400`

| packet length | packet type | uuid | sprint/stop | 
| - | - | - | - |
| 06 | 001e | ea0f | 0400 | 

> UUID part is quite weird, just copy this current thing one for one

---
### Switch to hotbar slot

Eg.
`04 002800 08` 

| packet length | packet type | slot number | 
| - | - | - |
| 04 | 002800 | 08 |

> slot number ranges from 00-08 (1-9)

