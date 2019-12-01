DEBUG = True
JSON_AS_ASCII = False

SQLITE_DATABASE = 'db.sqlite'

MYSQL_DATABASE_HOST = ''
MYSQL_DATABASE_USER = ''
MYSQL_DATABASE_PASSWORD = ''
MYSQL_DATABASE_DB = ''

QUERY_CREATE = """create table if not exists entry(
    id integer primary key autoincrement,
    title text not null,
    content text not null)
"""
QUERY_INSERT = """insert into entry(title, content)
    values('제목1', '내용1
내용1
내용1
내용1
내용1
내용1
내용1
내용1
내용1')
"""
