# boot.py - - runs on boot-up
import utils
import network
import utime
ssid = ""
wp2_pass = ""

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
nets = sta_if.scan()

for net in nets:
    if net[0].decode() == ssid:
        sta_if.connect(ssid, wp2_pass)
        utime.sleep(5)
        while True:
            if sta_if.isconnected():
                break

