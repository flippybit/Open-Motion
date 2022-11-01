# CANbus on Linux 101 Guide
CANbus is a very usefull protocol used for comunication mainly in automation
with only 2 wires it permits the comunication of many devices it is fast and reliable,
this protocol is used by our robot to comunicate with the wheel drivers,even though its so great it can be tricky to get it set up and working. but Fear not ! 

## This is a guide to get started with CANbus on linux
we will explore some of the linux commands needed to do some basic tests first with no hardware involved then with a canbus analyser 

###  No hardware required.
to do some test with this protocols all we need is a linux machine and the following packages intalled:
## 1. Install `can-utils` package
```bash
sudo apt install can-utils
```
`can-utils`  
this package will give us access to:    
*  candump: dumps on the stdout all messages recieveid
*  cansend: sends CAN messages "obviously" 
*  canbusload: TODO

## 2. Check your ip interfaces 
open a terminal and add the following commands:     
```bash
ip link
```
your output will be something similar to this:  
```bash
(base) fire@fire-box:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether A2:3e:99:00:tt:dd brd ff:ff:ff:ff:ff:ff
```
in my case we can see my `lo` loopback interface and my `enp5s0` ethernet conexion to the internet next we will add a new interface

## 3.   Create a virtual CANbus interface
To add a new interface use the this command **as sudo**
```bash
sudo ip link add dev vcan0 type vcan
```
what this does:
* It creates a new network interface `sudo ip link add`
* We pair it with a device called `dev vcan0` *virtual canbus* but u can call it whatever u like
* We define the type of device it is `type vcan`

    ## 3.1 check your network interfaces again
    if everything whent well your new interface should appear like so 
    ```bash
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    
    2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether b4:2e:99:0d:54:46 brd ff:ff:ff:ff:ff:ff
    
    3: vcan0: <NOARP> mtu 72 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/can
    ```
    **now dont forget to bring up the conexion !**
    ```bash
    sudo ip link set up vcan0
    ```
    if you check your networks interface again the state should of changed from DOWN to UP

## 4. Send and recieve packets from vcan0 using can-utils
For the final part we will play around with can utils to get our feet wet with the protocol.

### 4.1. First create fake can mesagges with `cangen` 
with a new termianl type the following to start sending fake messasges to our virtual canbus `vcan`
```bash
cangen vcan0
```
what now ? to  be able to see the messages you need to open a new terminal (dont shut this one)
### 4.2 Visualize messages using `candump`
open another terminal and type the follwing command to see what `vcan0` is recieving
```bash
candump vcan0
```
you should be able to see the messages incoming from cangen terminal like so:
```bash
(base) fire@fire-box:~$ candump vcan0
  vcan0  491   [7]  80 CB 18 05 99 4F 8A
  vcan0  473   [8]  E9 2B 8C 53 FD F2 C3 63
  vcan0  3EA   [8]  53 17 2E 46 FE 38 99 50
  vcan0  56E   [2]  48 15
  vcan0  5CC   [4]  B2 F3 B2 45
  vcan0  796   [8]  21 22 5D 33 79 E3 BF 69
  vcan0  68E   [8]  80 1F 03 2D 37 7C 31 21
  vcan0  7D0   [8]  AC C1 14 09 61 44 F2 11
  vcan0  623   [8]  FB 93 7C 27 96 AA ED 31
  vcan0  1E9   [4]  94 9D B1 15
  vcan0  181   [7]  D2 2E B6 46 EF 1E 37
  vcan0  31A   [8]  95 C2 1B 73 E6 D8 85 6F
  vcan0  54E   [7]  FF 02 24 20 E4 C4 AF
  vcan0  446   [0] 
  vcan0  6C8   [8]  0B FF E6 03 98 1E CC 18
  vcan0  47A   [7]  FA 62 BE 2A 9E 32 C9
  vcan0  5E3   [5]  34 DD B6 28 CD
  vcan0  6D9   [8]  A1 A5 79 49 5B 38 EC 6D
  vcan0  7B0   [3]  4A 57 23
``` 
there you have a bunch of can messages with random ID's and payloads
finally to stop use ctrl+c to stop.

**EOF.**