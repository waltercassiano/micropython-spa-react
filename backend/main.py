import os
import network
import picoweb
import ulogging as logging
import ure as re
import mimes
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
    print('network config:', ap.ifconfig())
    

def do_connect_wifi():
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_passowrd)
    print('network config:', sta_if.ifconfig())

def getIpEspServerEsp(ifconfig):
    ifconfiglist = list(ifconfig)
    print('Webapp Server ip:', str(ifconfiglist[0]))
    return str(ifconfiglist[0])

def wait_connect():
    while True:
        if sta_if.isconnected() == True:
            break
        if ap.isconnected() == True:
            break

def qs_parse(qs):
    parameters = {}
    ampersandSplit = qs.split("&")

    for element in ampersandSplit:
        equalSplit = element.split("=")
        parameters[equalSplit[0]] = equalSplit[1]
    return parameters

## ----- PICOWEB
def static_files_gzip(req, resp):
    file_path = "build/" + req.url_match.group(1)
    file_mime_type = mimes.mime_content_type(file_path)
    headers = b"Cache-Control: max-age=86400\r\n"
    if b"gzip" in req.headers.get(b"Accept-Encoding", b""):
        file_path += ".gz"
        headers += b"Content-Encoding: gzip\r\n"

    yield from app.sendfile(resp, file_path, file_mime_type, headers)
    
ROUTES = [
    ("/", lambda req, resp: (yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n" ))),
    (re.compile('^\/(.+\.css)$'), static_files_gzip),
    (re.compile('^\/(.+\.js)$'), static_files_gzip),
    (re.compile('^\/(.+\.png|.+\.jpeg|.+\.svg)$'), static_files_gzip) 
]
app = picoweb.WebApp(__name__, ROUTES)

def run_rest(ip):
    app.run(host=ip, debug=1)

# Setup WIFI 
# do_connect_wifi()

do_connect_ap()
wait_connect()


if sta_if.isconnected() == True:
    webapp_ip = getIpEspServerEsp(sta_if.ifconfig())

if ap.isconnected() == True:
    webapp_ip = getIpEspServerEsp(ap.ifconfig())   

run_rest(webapp_ip)
