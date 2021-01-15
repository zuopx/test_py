# coding=utf-8
'''对已有表加入新字段

sqlite官方说明：sqlite仅支持ALTER TABLE指令的部分功能，比如重命名表名，增加新列。
如果要实现列的重命名、删除和修改，需要组合其它指令。
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


# def test_rename(cur):
#     cur.execute('create table test(name text unique)')
#     print cur.execute('pragma table_info(test)').fetchall()
#     cur.execute('alter table test rename to test1')
#     print cur.execute('pragma table_info(test1)').fetchall()

def test_add(cur):
    cur.execute('create table test(name text not null unique)')
    cur.execute('insert into test values("test1")')
    cur.execute('alter table test add column password text')
    print cur.execute('pragma table_info(test)').fetchall()
    print cur.execute('select * from test').fetchall()

if __name__ == "__main__":
    prefix = __file__ + '::'
    pytest.main([__file__, '-s'])