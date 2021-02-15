import pyb
import time
import machine
import micropython

micropython.alloc_emergency_exception_buf(100)

baud = 1250000  # 125000  # 125000
bittime = 1/baud

# bs1, bs2 should total 10-1
TqCt = 10
BS1 = int(0.875*TqCt)
BS2 = TqCt - 1 - BS1

# bittime = (1+ bs1 + bs2) * tq
tq = bittime / (1+BS1+BS2)
PCLK1 = pyb.freq()[2]   # 30,000,000

# tq = prescaler/PCLK1  (it seems that only integer prescaler values work)
prescaler = PCLK1 * tq

print('tq {}  BS1 {}  BS2 {}  prescaler {}'.format(tq, BS1, BS2, prescaler))

can = pyb.CAN(1, pyb.CAN.NORMAL, auto_restart=True, extframe=False,
              prescaler=int(prescaler), bs1=BS1, bs2=BS2)
can.setfilter(0, pyb.CAN.LIST16, 0, (123, 124, 125, 126))

message = b'message'
print('sending ', message)
can.send(message, 123)

buf = ''
ary = [-1, -1, -1, memoryview(buf), buf]


def cb(bus, reason):

    global ary
    try:
        bus.recv(0, ary)
    except Exception as e:
        print('Exception', e)

    micropython.schedule(cb_sched, None)


def cb_sched(_):

    msg_id, is_rtr, FMI, _, buf = ary[0:5]
    print('recieved ', buf)
    print('id {} rtr {} FMI {}'.format(msg_id, is_rtr, FMI))


can.rxcallback(0, cb)

print('waiting for message')
while True:
    # time.sleep(1)
    machine.idle()
