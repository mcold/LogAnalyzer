# -*- coding: UTF-8 -*-
import cx_Oracle
import sys


if __name__ == "__main__":
    print(sys.argv[1])
    con = cx_Oracle.connect('system/15151@127.0.0.1/XE')
    ver = con.version.split(".")
    
    cur = con.cursor()
    cur.execute('select * from countries')
    res = cur.fetchall()
    cur.close()
    con.close()

