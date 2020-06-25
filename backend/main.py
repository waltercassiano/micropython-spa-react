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
import uhashlib

logging.basicConfig(level=logging.DEBUG)

user_service.add_user("admin", "123456")

CORS_ENABLED = True

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

def generate_access_token(data_to_token):
    return utils.decode(ubinascii.hexlify((uhashlib.sha1(data_to_token).digest())))

def require_access_token(func):
    def access_token_validade(req, resp):
        db_access_token = config_service.get_active_user("access_token")
        header_access_token = req.headers.get(b"access_token")

        return
        if not db_access_token or not header_access_token:
            yield from picoweb.start_response(resp, status="401")
            yield from resp.awrite('{ "msg" : "invalid access token"}')
            return

        db_access_token = db_access_token.get("access_token")

        if header_access_token != db_access_token:
            yield from picoweb.start_response(resp, status="401")
            yield from resp.awrite('{ "msg" : "invalid access token"}')
            return


        yield from func(req, resp)

    return access_token_validade

def require_auth(func):
    def auth(req, resp):
        auth = req.headers.get(b"Authorization")

        if not auth:
            yield from resp.awrite('{ "msg" : "wrong user or password"}')
            yield from picoweb.start_response(resp, status="401")
            return

        auth = ubinascii.a2b_base64(auth).decode()
        client_id, client_secrect = auth.split(":", 1)

        username = req.headers.get(b"username")
        pwd = req.headers.get(b"pwd")

        if not username or not pwd:
            yield from picoweb.start_response(resp, status="401")
            yield from resp.awrite('{ "msg" : "wrong user or password"}')
            return

        username = username.decode('utf-8')
        pwd = pwd.decode('utf-8')

        if client_id != _client_id or client_secrect != _client_secret:
            yield from picoweb.start_response(resp, status="401")
            yield from resp.awrite('{ "msg" : "wrong user or password"}')
            return

        if not user_service.auth_user(username, pwd):
            yield from picoweb.start_response(resp, status="401")
            yield from resp.awrite('{ "msg" : "wrong user or password"}')
            return

        access_token = generate_access_token(username + ":" + pwd)
        config_service.save_active_user("access_token", access_token)
        yield from func(req, resp)
        yield from resp.awrite('{"access_token": "' + access_token + '"}')

    return auth

def cors(func):
    def _cors(req, resp):
        if CORS_ENABLED is not True:
            yield from func(req, resp)
        header  = b"Access-Control-Allow-Origin: *\r\n"
        header += b"Access-Control-Allow-Method: POST, DELETE, PUT, GET\r\n"
        header += b"Access-Control-Allow-Headers: *\r\n"
        if req and req.method == "OPTIONS":
            yield from picoweb.start_response(resp, content_type="text/html; charset=utf-8", status="200", headers=header)
            return
        yield from func(req, resp)
    return _cors

def start_response(req, resp):
    if CORS_ENABLED is not True:
        yield from picoweb.start_response(resp)
        return
    yield from picoweb.start_response(resp, headers = b"Access-Control-Allow-Origin: *\r\n")

@app.route(re.compile("/api/access-token"))
@cors
@require_auth
def handle_api_request(req, resp):
    yield from start_response(req, resp)

@app.route("/api/config/wifi")
@require_access_token
def route_api(req, resp):
    yield from start_response(req, resp)

@app.route(re.compile('\/(.+\.js|.+\.css|.+\.png|.+\.jpeg|.+\.svg)$'))
def static_files_gzip(req, resp):
    file_path = "build/" + req.url_match.group(1)
    file_mime_type = mime_content_type(file_path)

    headers = b"Cache-Control: max-age=100\r\n"
    if b"gzip" in req.headers.get(b"Accept-Encoding"):
        file_path += ".gz"
        headers += b"Content-Encoding: gzip\r\n"

    yield from app.sendfile(resp, file_path, file_mime_type, headers)

@app.route("/")
def frontend(req, resp):
    yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n")

@app.route("/")
def serve_spa_frontend(req, resp):
    yield from app.sendfile(resp, "/build/index.html.gz", "text/html", b"Content-Encoding: gzip\r\n")



# Setup WIFI
do_connect_wifi()
#do_connect_ap()
wait_connect()

if sta_if.isconnected() is True:
    webapp_ip = getIpEspServerEsp(sta_if.ifconfig())

if ap.isconnected() == True:
    webapp_ip = getIpEspServerEsp(ap.ifconfig())

if __name__ == "__main__":
    app.run(host=webapp_ip, port=3000, debug=1)
