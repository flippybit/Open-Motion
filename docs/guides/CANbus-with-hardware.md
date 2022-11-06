#   Conecting Linux with CANbus USB-CAN Analyzer
In this guide we will cover all the necesary steps to configure our USB-CAN Analyzer with Linux, this model is very cheap and sold everywhere so ill cover its configuration as it may help others with other projects.

## Commands to hunt for the device in the jungle of linux files
###  `dmesg` : display the kernel ring buffer 
    *   in our case use with grep `dmesg | grep tty` to find  the usb device with the analyzer
  ```bash
  (open-motion) fire@fire-box:~/open-motion$ dmesg|grep tty
[    0.000000] printk: console [tty0] enabled
[    2.322796] 00:03: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    5.875842] cdc_acm 3-4:1.0: ttyACM0: USB ACM device
#[    5.903412] usb 3-1: ch341-uart converter now attached to ttyUSB0
  ```
### `lsusb`: list the usb devices conected to the system 

```bash
(open-motion) fire@fire-box:~/open-motion$ lsusb
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 003: ID 2341:0043 Arduino SA Uno R3 (CDC ACM)
#Bus 003 Device 002: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

## Mount CANusb serial adapter

to be able to use this adaptor with can-utils and ROS we must mount it using,  
`slcand`: userspace daemon for serial line CAN interface driver SLCAN.

```bash
sudo slcand -o -c -s5 /dev/ttyUSB0
```
### check if the mounting was sucessfull

```bash
ip link
```
**output should be**
```bash
(open-motion) fire@fire-box:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether b4:2e:99:0d:54:46 brd ff:ff:ff:ff:ff:ff
3: vcan0: <NOARP,UP,LOWER_UP> mtu 72 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/can 
4: slcan0: <NOARP> mtu 16 qdisc noop state DOWN mode DEFAULT group default qlen 10
    link/can 
```
### Bring up the interface.
```bash
ip link slcan0 up
```