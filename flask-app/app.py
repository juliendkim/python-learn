from flask import Flask, jsonify, Response, json
import os
import sqlite3

app = Flask(__name__)
app.config.from_pyfile(os.path.join(app.root_path, 'config.py'))


def connect_db():
    con = sqlite3.connect(os.path.join(app.root_path, app.config['SQLITE_DATABASE']))
    con.execute(app.config['QUERY_CREATE'])
    con.commit()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con, cur


@app.route('/')
def show_all():
    con, cur = connect_db()
    cur.execute('select id, title, content from entry')
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append(dict(row))
    return Response(json.dumps(data, ensure_ascii=False), content_type='application; charset=utf-8')


@app.route('/add')
def add():
    con, cur = connect_db()
    cur.execute(app.config['QUERY_INSERT'])
    con.commit()
    return jsonify({'code': 0, 'result': 'added'})


if __name__ == '__main__':
    app.run()
