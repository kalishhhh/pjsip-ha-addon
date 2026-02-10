from flask import Flask, request, jsonify
import pjsua2 as pj
import json
import threading
import time

with open("/data/options.json") as f:
    cfg = json.load(f)

SERVER = cfg["server_ip"]
EXT = cfg["extension"]
PASS = cfg["password"]

app = Flask(__name__)

ep = pj.Endpoint()
ep.libCreate()

ep_cfg = pj.EpConfig()
ep_cfg.uaConfig.maxCalls = 1
ep.libInit(ep_cfg)

transport = pj.TransportConfig()
transport.port = 5060
ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, transport)

ep.libStart()

acc_cfg = pj.AccountConfig()
acc_cfg.idUri = f"sip:{EXT}@{SERVER}"
acc_cfg.regConfig.registrarUri = f"sip:{SERVER}"

cred = pj.AuthCredInfo("digest", "*", EXT, 0, PASS)
acc_cfg.sipConfig.authCreds.append(cred)

account = pj.Account()
account.create(acc_cfg)

current_call = None
lock = threading.Lock()


@app.route("/call", methods=["POST"])
def make_call():
    global current_call
    number = request.json["number"]

    with lock:
        call = pj.Call(account)
        prm = pj.CallOpParam(True)
        call.makeCall(f"sip:{number}@{SERVER}", prm)
        current_call = call

    return jsonify({"status": "calling"})


@app.route("/answer", methods=["POST"])
def answer():
    with lock:
        if current_call:
            prm = pj.CallOpParam()
            prm.statusCode = 200
            current_call.answer(prm)
    return jsonify({"status": "answered"})


@app.route("/hangup", methods=["POST"])
def hangup():
    with lock:
        if current_call:
            prm = pj.CallOpParam()
            prm.statusCode = 486
            current_call.hangup(prm)
    return jsonify({"status": "hungup"})


def keep_alive():
    """Keep PJSIP alive."""
    while True:
        ep.libHandleEvents(50)


def keep_alive():
    while True:
        time.sleep(1)

threading.Thread(target=keep_alive, daemon=False).start()

app.run(host="0.0.0.0", port=8080, threaded=True)

