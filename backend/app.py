import os, time
from flask import Flask, Response, send_from_directory

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


messeges = ["Hello,", " How", " are", " you!", " What", " can", " I do", " for you?"]


def generate():
    for message in messeges:
        yield f'0:"{message}"\n'
        time.sleep(0.2)
    yield 'e:{"finishReason":"stop","usage":{"promptTokens":null,"completionTokens":null}}\n'
    yield 'd:{"finishReason":"stop","usage":{"promptTokens":null,"completionTokens":null}}\n'


@app.route("/api/chat", methods=["POST"])
def chat():
    return Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
