from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/hello")
@app.route("/hello/<username>")
def hello_world2(username=None):
    # return "Hello, World! {}!".format(username)
    return render_template("hello.html", username=username)


@app.route("/post", methods=["POST", "PUT", "DELETE"])
def show_post():
    # ユーザーが post に投げた値を取り出せる
    return str(request.values)


def main():
    app.debug = True
    app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
