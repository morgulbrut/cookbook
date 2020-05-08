#!/usr/bin/env python3

import yaml # install with pip install pyaml
from pprint import pprint # python pretty printer

with open('example.yaml', 'r') as stream:
    try:
        settings = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)


pprint(settings)

for uC in settings['uCs']:
    print("=========== Programming {} ===========".format(uC['name']))
    tool = uC['flasher']['path']
    args = " ".join(uC['flasher']['args'])
    print(tool)
    print(args)
    print("[CMD]: {} {} {}".format(tool,args, uC['hexfile']))

