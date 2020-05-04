import os
import network
import picoweb
import ulogging as logging
import ure as re
import mimes
import utils
import ujson
from db import Mydb
logging.basicConfig(level=logging.DEBUG)

# Networks WIFI and acess point
sta_if = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

# WEBAPP IP
webapp_ip = ""

# Access point Setup
ap_ssid = 'react-iot'
ap_password = '123456'


# Wifi Setup
wifi_ssid = ""
wifi_passowrd = ""

def do_connect_ap():
    if not ap.isconnected():
        ap.active(True)
        ap.config(essid=ap_ssid, password=ap_password)


def do_connect_wifi():
    if not sta_if.isconnected():
        sta_if.active(True)
        print(getWifi(sta_if.scan()))
        sta_if.connect(wifi_ssid, wifi_passowrd)

def getIpEspServerEsp(ifconfig):
    ifconfiglist = list(ifconfig)
    return str(ifconfiglist[0])

def wait_connect():
    while True:
        if sta_if.isconnected() is True:
            break
        if ap.isconnected() is True:
            break

def getWifi(wifiListDetected):
   return list(map(lambda wifi: utils.decode(wifi[0]), wifiListDetected))

app = picoweb.WebApp(__name__, serve_static=False)

@app.route(re.compile('^(.+static.+)$'))
def static_files_gzip(req, resp):
    file_path = "build/" + req.url_match.group(1)
    file_mime_type = mimes.mime_content_type(file_path)
    headers = b"Cache-Control: max-age=86400\r\n"
    if b"gzip" in req.headers.get(b"Accept-Encoding", b""):
        file_path += ".gz"
        headers += b"Content-Encoding: gzip\r\n"

    yield from app.sendfile(resp, file_path, file_mime_type, headers)

@app.route("/")
def serve_spa_frontend(req, resp):
    yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n")

@app.route("/api/config/wifi")
def route_api(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(ujson.dumps(getWifi(sta_if.scan())))


# Setup WIFI
do_connect_wifi()

#do_connect_ap()
wait_connect()

if sta_if.isconnected() is True:
    webapp_ip = getIpEspServerEsp(sta_if.ifconfig())

if ap.isconnected() is True:
    webapp_ip = getIpEspServerEsp(ap.ifconfig())

if __name__ == "__main__":
    app.run(host=webapp_ip, port=3000, debug=1)
