from flask import Flask, jsonify, request, abort, make_response
from flask import render_template
import socket

TEMPLATES_FOLDER = 'templates'
STATICS_FOLDER = 'static'
app = Flask(__name__, static_url_path='', static_folder=STATICS_FOLDER, template_folder=TEMPLATES_FOLDER)

BACKGROUND_IMAGE = "under_water.png"
CSS_FILE =  "blue"


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
    return render_template('index.html', theme=CSS_FILE, background_image='../images/'+BACKGROUND_IMAGE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # os.system("python cpu_task.py &")

    # os.spawnl(os.P_DETACH, 'python', 'cpu_task.py')
    # processes = cpu_count()
    # mem = virtual_memory()
    # print("Memory=" + str(mem.total/1024/1024/1024))  # total physical memory available
    # print('utilizing %d cores\n' % processes)
    #generate_load()
