# How to bind a USB device under a static name

Long story short, use a udev rule

* https://unix.stackexchange.com/questions/66901/how-to-bind-usb-device-under-a-static-name
* http://www.reactivated.net/writing_udev_rules.html#example-camera

Example for for an FTDI and an Adafruit Feather M4 Express

```
  ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="FTDI"
  ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="1d6b", ATTRS{idProduct}=="0002", SYMLINK+="FeatherM4"
```

after reloading all the stuff they show up as `/dev/FTDI` and `/dev/FeatherM4`
