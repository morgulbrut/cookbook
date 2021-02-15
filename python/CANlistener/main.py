#!/usr/bin/python3
# -*- coding: utf-8 -*-

import can
from can.listener import Listener
from colorama import Fore, Style, init
import sys


class CanListener(Listener):
    ids = []

    def set_ids(ids):
        print(Fore.YELLOW + "Set filter on {}".format(ids))
        self.ids = ids

    def on_message_received(self, msg):
        if msg.arbitration_id in self.ids:
            print("{}: {}".format(msg.msg.arbitration_id, msg.data))


if __name__ == "__main__":
    init(autoreset=True)

    # print(Fore.GREEN + banner)
    try:
        if platform.system() == "Linux":
            bus = can.interface.Bus(bustype="socketcan", channel="can0")
        if platform.system() == "Windows":
            bus = can.interface.Bus(
                bustype="pcan", channel="PCAN_USBBUS1", bitrate=1000000)
    except:
        print(Fore.RED + "CAN Adapter Verbunden?")
        sys.exit()

    # Attach the listender
    listener = CanListener()
    listener.set_ids(sys.argv[1:])
    notifier = can.Notifier(bus, [listener])
