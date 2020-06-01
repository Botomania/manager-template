import sys
import json

from flask import Flask, request, jsonify

from errors import panic, errors

try:
    from manager import Manager
except ImportError as e:
    print(e)
    panic(errors.MANAGER_IMPORT_ERROR)

app = Flask(__name__)
m = None


@app.route("/init", methods=["POST"])
def init():
    global m

    params = request.json
    players = params["players"]

    m = Manager(players)

    return jsonify({"success": True})


@app.route("/action", methods=["POST"])
def act():
    player = request.json["player"]
    action = request.json["action"]
    return m.manage(player, action)


@app.route("/state", methods=["GET"])
def state():
    return m.get_state()


@app.route("/invalid", methods=["POST"])
def invalid():
    player = request.json["player"]
    m.invalidate(player["id"])

    return json.dumps({"success": True})


@app.route("/quit", methods=["POST"])
def quit():
    sys.exit(0)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
