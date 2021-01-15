# coding=utf-8
'''Python2 和 sqlite3 数据类型转换。
NONE <--> NULL
int/long <--> INTEGER
float <--> REAL
str,unicode <--> TEXT
datetime.date --> DATE
datetime.datetime --> TIMESTAMP
unicode <-- DATE
unicode <-- TIMESTAMP
'''
import sqlite3
import datetime


def test_datetime():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    cur.execute('create table test(d date, ts timestamp)')

    today = datetime.date.today()
    now = datetime.datetime.now()
    cur.execute('insert into test(d, ts) values(?, ?)', (today, now))
    cur.execute('select d, ts from test')
    row = cur.fetchone()
    print today, '=>', row[0], type(row[0])
    print now, '=>', row[1], type(row[1])

    cur.execute('select current_date, current_timestamp')
    row = cur.fetchone()
    print row[0], type(row[0])
    print row[1], type(row[1])

    cur.close()
    conn.close()


if __name__ == "__main__":
    test_datetime()
