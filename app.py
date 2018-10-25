from flask import Flask, jsonify, request, abort, make_response
from flask import render_template
import socket
import os

TEMPLATES_FOLDER = 'templates'
STATICS_FOLDER = 'static'
app = Flask(__name__, static_url_path='', static_folder=STATICS_FOLDER, template_folder=TEMPLATES_FOLDER)

BACKGROUND_IMAGE = "under_water.png"
# CSS_FILE = "blue"

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

APP_NAME = "APP_NAME" in os.environ and os.environ.get('APP_NAME') or "Connectivity Test App"
BG_COLOR = "BG_COLOR" in os.environ and os.environ.get('BG_COLOR') or "blue"


def socket_test(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host, port))
    except Exception as ex:
        print('Unable to connect ' + str(ex))
        return {"status": False, "message": str(ex)}

    return {"status": True, "message": "Success!"}


@app.route('/test', methods=['POST'])
def test():
    json_data = request.get_json(silent=True)

    test_results = socket_test(json_data["host"], json_data["port"])

    if test_results["status"]:
        return jsonify(test_results)
    else:
        return abort(make_response(jsonify(test_results), 400))


@app.route('/')
def main():
    try:
        return render_template('index.html', theme=BG_COLOR, background_image='../images/'+BACKGROUND_IMAGE, app_name=APP_NAME, backgroundcolor=color_codes[BG_COLOR])
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)