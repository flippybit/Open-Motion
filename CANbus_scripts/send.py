
import os
import can
import time

#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)

# os.system('sudo ifconfig can0 down')
# os.system('sudo ip link set can0 type can bitrate 500000')
# os.system("sudo ifconfig can0 txqueuelen 100000")
os.system('sudo ifconfig can0 up')


can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
send_count = 0


#SYNCHRONOUS VELOCITY CONTROL INITIALIZATION
set_sync_control = [0x2B, 0x0F, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00]  #      2B 0F 20 00 01 00 00 00
msg_sync_control = can.Message(arbitration_id=0x601, data=set_sync_control, is_extended_id=False)

set_profile_vel_mode = [0x2F, 0x60, 0x60, 0x00, 0x03, 0x00, 0x00, 0x00] #   2F 60 60 00 03 00 00 00
msg_profile_vel_mode = can.Message(arbitration_id=0x601, data=set_profile_vel_mode, is_extended_id=False)

#Motor accel settings
set_right_accel_time = [0x23, 0x83, 0x60, 0x02, 0x64, 0x00, 0x00, 0x00] #   23 83 60 02 64 00 00 00 -->100ms
msg_right_accel_time = can.Message(arbitration_id=0x601, data=set_right_accel_time, is_extended_id=False)

# Target Speed run
set_target_speed_slow = [0x23, 0xFF, 0x60, 0x03, 0x0A, 0x00, 0xF6, 0xFF]#   23 FF 60 03 00 64 00 00
msg_target_speed = can.Message(arbitration_id=0x601, data=set_target_speed_slow, is_extended_id=False)

# Enable motors
en_0 = [0x2B, 0x40, 0x60, 0x00, 0x06, 0x00, 0x00, 0x00]
en_1 = [0x2B, 0x40, 0x60, 0x00, 0x07, 0x00, 0x00, 0x00]
en_2 = [0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00, 0x00, 0x00]
msg_0 = can.Message(arbitration_id=0x601, data=en_0, is_extended_id=False)
msg_1 = can.Message(arbitration_id=0x601, data=en_1, is_extended_id=False)
msg_2 = can.Message(arbitration_id=0x601, data=en_2, is_extended_id=False)

# Motor stop 
motor_stop = [0x2B, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00] #2b 40 60 00 00 00 00 00 motor stop and disable
msg_motor_stop = can.Message(arbitration_id=0x601, data=motor_stop, is_extended_id=False)

# Get modes of operation

while True:
    option = input("> ")
    
    if option == 'set':
        print("set sync control and accel time 100ms")
        can0.send(msg_sync_control)
    
    if option == 'runslow':
        print("run slow  sent:")
        can0.send(msg_target_speed)
    
    if option == 'en':
        print("motors enabled !")
        can0.send(msg_0)
        can0.send(msg_1)
        can0.send(msg_2)

    if option =='stop':
        print("motor stop")
        can0.send(msg_motor_stop)

    if option =='exit':
        print("bye bye ! ")
        break

    
    time.sleep(0.001)

os.system('sudo ifconfig can0 down')