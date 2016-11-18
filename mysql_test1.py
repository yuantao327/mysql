# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
con = mdb.connect('localhost', 'root','', 'test');
with con:

    #获取连接的 cursor，只有获取了 cursor，我们才能进行各种操作
    cur = con.cursor()
    #创建一个数据表 writers(id,name)
    cur.execute("DROP TABLE Writers")

    cur.execute("CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")

    #以下插入了 5 条数据
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

    #类似于其他语言的 query 函数， execute 是 python 中的执行查询函数
    cur.execute("SELECT * FROM Writers")

    #使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
    rows = cur.fetchall()

    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    for row in rows:
        print row

con.close()