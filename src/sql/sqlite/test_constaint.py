# coding=utf-8
'''定义表时的约束
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
DEFAULT
CHECK
'''
import sqlite3
import pytest


@pytest.fixture()
def cur():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    yield cur
    cur.close()
    conn.close()


def test_unique(cur):
    cur.execute('create table test(name text unique)')
    cur.execute('insert into test values(?)', ('test1',))
    with pytest.raises(sqlite3.IntegrityError):
        cur.execute('insert into test values(?)', ('test1',))


def test_default(cur):
    cur.execute('create table test(name text, password text default "123")')
    cur.execute('insert into test(name) values(?)', ('test1',))
    row = cur.execute('select * from test').fetchone()
    assert row[1] == '123'


def test_check(cur):
    cur.execute('create table test(salary real check(salary > 0))')
    cur.execute('insert into test values(?)', (10, ))
    with pytest.raises(sqlite3.IntegrityError):
        cur.execute('insert into test values(?)', (-10, ))


if __name__ == "__main__":
    prefix = __file__ + '::'
    pytest.main([prefix + 'test_check', '-s'])
