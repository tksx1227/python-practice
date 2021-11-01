import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)


# データベースをグローバルで管理する
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("test_sqlite.db")
    return db


# アプリケーションの終了時にデータベースも閉じる（デコレータ）
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/employee", methods=["POST", "PUT", "DELETE"])
@app.route("/employee/<name>", methods=["GET"])
def employee(name=None):
    # 練習用として、ここでテーブルを作成する
    db = get_db()
    curs = db.cursor()
    curs.execute(
        "CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
    )
    db.commit()

    name = request.values.get("name", name)
    # GETリクエスト時にはデータベースからデータを取得して返す
    if request.method == "GET":
        curs.execute(f"SELECT * FROM persons WHERE name='{name}'")
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return f"{user_id}:{name}"

    # POSTリクエスト時にはデータベースへデータを追加する
    if request.method == "POST":
        curs.execute(f"INSERT INTO persons(name) VALUES('{name}')")
        db.commit()
        return f"created {name}", 201

    # PUTリクエスト時にはデータを更新する
    if request.method == "PUT":
        new_name = request.values["new_name"]
        curs.execute(f"UPDATE persons SET name='{new_name}' WHERE name='{name}'")
        db.commit()
        return f"updated {name}: {new_name}", 200

    # DELTEリクエスト時にはデータを削除する
    if request.method == "DELETE":
        curs.execute(f"DELETE FROM persons WHERE name='{name}'")
        db.commit()
        return f"deleted {name}", 200

    curs.close()


@app.route("/")
def hello_world():
    return "Hello, World!"


# HTMLのテンプレートファイルを使用する例
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
