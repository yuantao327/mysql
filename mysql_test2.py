# -*- coding: UTF-8 -*-
#This is a test
#��װ MYSQL DB for python
import MySQLdb as mdb
con = None
try:
  #���� mysql �ķ����� connect('ip','user','password','dbname')
  con = mdb.connect('localhost', 'root','', 'test');

  #���еĲ�ѯ���������� con ��һ��ģ�� cursor �������е�
  cur = con.cursor()

  #ִ��һ����ѯ
  cur.execute("SELECT VERSION()")
  #ȡ���ϸ���ѯ�Ľ�����ǵ������

  data = cur.fetchone()
  print "Database version : %s " % data
finally:
  if con:
    #������Σ����Ӽǵùر�
    con.close()
