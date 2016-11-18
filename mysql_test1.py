# -*- coding: utf-8 -*-
# This is my test for Mysql
import MySQLdb as mdb
import sys
con = mdb.connect('localhost', 'root','', 'test');
with con:

    #��ȡ���ӵ� cursor��ֻ�л�ȡ�� cursor�����ǲ��ܽ��и��ֲ���
    cur = con.cursor()
    #����һ�����ݱ� writers(id,name)
    cur.execute("DROP TABLE Writers")

    cur.execute("CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")

    #���²����� 5 ������
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

    #�������������Ե� query ������ execute �� python �е�ִ�в�ѯ����
    cur.execute("SELECT * FROM Writers")

    #ʹ�� fetchall �����������������άԪ�飩���� rows ����
    rows = cur.fetchall()

    #���α��������������ÿ��Ԫ�أ����Ǳ��е�һ����¼����һ��Ԫ������ʾ
    for row in rows:
        print row

con.close()