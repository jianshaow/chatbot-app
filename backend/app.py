import os, time, json
from flask import Flask, Response, send_from_directory

from mock_data import pre_events, messeges, post_events

frontend = os.path.abspath(os.path.join("../frontend", "out"))
frontend = os.environ.get("FRONTEND_DIR", frontend)

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def main(path):
    print("path:", path)
    if path == "":
        return send_from_directory(frontend, "index.html")
    else:
        return send_from_directory(frontend, path)


def generate():
    for event in pre_events:
        yield f"8:{json.dumps(event)}\n"
        time.sleep(0.2)
    for message in messeges:
        yield f'0:"{message}"\n'
        time.sleep(0.2)
    for event in post_events:
        yield f"8:{json.dumps(event)}\n"
        time.sleep(0.2)


@app.route("/api/chat", methods=["POST"])
def chat():
    return Response(generate(), mimetype="text/plain")


@app.route("/api/chat/config", methods=["GET"])
def config():
    return {"starterQuestions": None}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
