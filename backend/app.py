import os
from flask import Flask, request, send_from_directory

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
