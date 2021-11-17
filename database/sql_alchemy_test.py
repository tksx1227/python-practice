import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


# 扱うデータベースを指定, echo=Trueで詳細が出力される
engine = sqlalchemy.create_engine("sqlite:///:memory:", echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()


# Base を継承してテーブルを作成する
class Person(Base):
    __tablename__ = "persons"

    # テーブルのカラムは sqlalchemy.Column で指定する
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# データの追加
p1 = Person(name="Mike")
session.add(p1)
p2 = Person(name="Nancy")
session.add(p2)
p3 = Person(name="Tomori")
session.add(p3)
session.commit()

# データの更新
p4 = session.query(Person).filter_by(name="Mike").first()
p4.name = "Michel"
session.add(p4)
session.commit()

# データの削除
p5 = session.query(Person).filter_by(name="Nancy").first()
session.delete(p5)
session.commit()

# データの取得
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
