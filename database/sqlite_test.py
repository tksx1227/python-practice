import sqlite3


# データベースに接続する
# 引数に ":memory:" を指定するとメモリ上にデータベースが作成される
# conn = sqlite3.connect("test_sqlite.db")
conn = sqlite3.connect(":memory:")

# データベースを操作するためのカーソルを作成する
curs = conn.cursor()

# executeにSQLを記述する
# データベースへの操作は、commitを行わないとファイルに反映されない
curs.execute(
    "CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
)
conn.commit()

curs.execute(
    "INSERT INTO persons(name) values('Mike')"
)
conn.commit()

curs.execute(
    "INSERT INTO persons(name) values('Nancy')"
)
curs.execute(
    "INSERT INTO persons(name) values('Takuma')"
)
conn.commit()

curs.execute("UPDATE persons SET name='Michel' WHERE name='Mike'")
conn.commit()

curs.execute("DELETE FROM persons WHERE name='Michel'")
conn.commit()

curs.execute("SELECT * FROM persons")
# fetchallでデータを取得できる
print(curs.fetchall())

# 最後にデータベースとカーソルの両方をクローズする
curs.close()
conn.close()
