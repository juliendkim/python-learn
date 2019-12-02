from flask import Flask
import os
import sqlite3
import flask_cors
# from flaskext.mysql import MySQL
#
app = Flask(__name__)
flask_cors.CORS(app)
app.config.from_pyfile(os.path.join(app.root_path, 'config.py'))
# mysql = MySQL()
# mysql.init_app(app)
#
#
# def connect_db():
#     con = sqlite3.connect(os.path.join(app.root_path, app.config['SQLITE_DATABASE']))
#     con.execute(app.config['QUERY_CREATE'])
#     con.commit()
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     return con, cur


@app.route('/')
def get():
    from flask import jsonify
    return jsonify({'str' : 'Hello World!'})


@app.route('/<name>')
def get_with_param(name):
    from flask import Response, json
    print("Hello %s!" % name)
    resdata = {'name': name}
    return Response(json.dumps(resdata, ensure_ascii=False), content_type='application; charset=utf-8')


# @app.route('/', methods=['POST'])
# def post_hello():
#     from flask import request, jsonify
#     print(request.json)
#     req = request.json
#     school = req["school"]
#     dept = req["department"]
#
#     resdata = {'s': school, 'd': dept, 'id': 1, 'name': 'asdf'}
#     return jsonify(resdata)
#
#
# @app.route('/view')
# def get_sqlite3():
#     from flask import Response, json
#     con, cur = connect_db()
#     cur.execute('select id, title, content from entry')
#     rows = cur.fetchall()
#     data = []
#     for row in rows:
#         data.append(dict(row))
#     return Response(json.dumps(data, ensure_ascii=False), content_type='application; charset=utf-8')
#
#
# @app.route('/add')
# def add():
#     from flask import jsonify
#     con, cur = connect_db()
#     cur.execute(app.config['QUERY_INSERT'])
#     con.commit()
#     return jsonify({'code': 0, 'result': 'added'})
#
#
# @app.route('/mysql')
# def get_mysql():
#     from flask import Response, json
#     query = 'select id, title, content from entry'
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     data = []
#     for row in rows:
#         data.append(dict(row))
#     return Response(json.dumps(data, ensure_ascii=False), content_type='application; charset=utf-8')
#
#
if __name__ == '__main__':
    app.run()
