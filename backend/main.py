import os
import network
import picoweb
import ulogging as logging
import ure as re
from mimes import mime_content_type
from app_esp import config_service, user_service
import ubinascii
import utils
import ujson

logging.basicConfig(level=logging.DEBUG)

user_service.add_user("admin", "123456")


logging.basicConfig(level=logging.DEBUG)

# Networks WIFI and acess point
sta_if = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

##
_client_id = "897DD9C9-F2CDB-CB4226245EC958AF"
_client_secret = "BBC344BA-28463-6F838E84419B6B81"

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

app = picoweb.WebApp(__name__, routes=None, serve_static=None)

def require_auth(func):
    def auth(req, resp):
        auth = req.headers.get(b"Authorization")
        if not auth:
            resp.awrite('{ "msg" : "wrong user or password"}')
            picoweb.http_error(resp, "401")
            return

        auth = ubinascii.a2b_base64(auth).decode()
        client_id, client_secrect = auth.split(":", 1)

        username = req.headers.get(b"username")
        pwd = req.headers.get(b"pwd")
        username = username.decode('utf-8')
        pwd = pwd.decode('utf-8')

        if (client_id != _client_id or client_secrect != _client_secret or user_service.auth_user(username, pwd) is not True):
            resp.awrite('{ "msg" : "wrong user or password"}')
            picoweb.http_error(resp, "401")
            return

        yield from func(req, resp)

    return auth

@app.route(re.compile("/api/access-token"))
@require_auth
def handle_api_request(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite('{ "msg" : "logged with success" }')

@app.route(re.compile('\/(.+\.js|.+\.css|.+\.png|.+\.jpeg|.+\.svg)$'))
def static_files_gzip(req, resp):
    file_path = "build/" + req.url_match.group(1)
    file_mime_type = mime_content_type(file_path)

    headers = b"Cache-Control: max-age=100\r\n"
    if b"gzip" in req.headers.get(b"Accept-Encoding", b""):
        file_path += ".gz"
        headers += b"Content-Encoding: gzip\r\n"

    yield from app.sendfile(resp, file_path, file_mime_type, headers)

@app.route("/")
def frontend(req, resp):
    yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n")

def run_rest(ip):
    app.run(host=ip, debug=1)

@app.route("/")
def serve_spa_frontend(req, resp):
    yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n")

@app.route("/api/config/wifi")
def route_api(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(ujson.dumps(getWifi(sta_if.scan())))


# Setup WIFI
# do_connect_wifi()
do_connect_ap()
wait_connect()

if sta_if.isconnected() is True:
    webapp_ip = getIpEspServerEsp(sta_if.ifconfig())

if ap.isconnected() == True:
    webapp_ip = getIpEspServerEsp(ap.ifconfig())

if __name__ == "__main__":
    app.run(host=webapp_ip, port=3000, debug=1)
