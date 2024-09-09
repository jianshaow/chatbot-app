import os
from flask import Flask, request, send_from_directory

frontend = os.path.abspath(os.path.join("../frontend", "out"))
frontend = os.environ.get("FRONTEND_DIR", frontend)
static_folder = os.path.join(frontend, "static")

app = Flask(__name__, static_folder=static_folder)


@app.route("/", defaults={"path": ""})
@app.route("/<path>")
def main(path):
    if path == "" or path == "setting":
        return send_from_directory(frontend, "index.html")
    else:
        return send_from_directory(frontend, path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
