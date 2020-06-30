from colorama import Fore, Style, init
import can
import sys
import time
import platform

banner = '''
       _________    _____   _______                       
  _____\_   ___ \  /  _  \  \      \   ____   ___________ 
 /  ___/    \  \/ /  /_\  \ /   |   \ /    \_/ __ \_  __ \\
 \___ \\\\     \___/    |    /    |    |   |  \  ___/|  | \/
/____  >\______  \____|__  \____|__  |___|  /\___  |__|   
     \/        \/        \/        \/     \/     \/    

CAN scanner

V 0.1
'''


def send_raw(addr, bus, data=[], length=0):
    msg = can.Message(arbitration_id=addr, data=data, extended_id=True)
    print(hex(msg.arbitration_id), msg.data)
    bus.send(msg)


if __name__ == "__main__":
    init(autoreset=True)
    print(Fore.GREEN + banner)

    if platform.system() == "Linux":
        bus = can.interface.Bus(bustype="socketcan", channel="can0")
    if platform.system() == "Windows":
        bus = can.interface.Bus(
            bustype="pcan", channel="PCAN_USBBUS1", bitrate=1000000)

    for id in range(0x4200000, 0x42000FF):
        send_raw(id, bus)
        time.sleep(0.3)
