# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 12:19:33 2015

@author: melo
"""
import pylab
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
    cur=conn.cursor()     
    conn.select_db('phpmyadmin') 
    cur.execute('select * from user_submit111')
    results=cur.fetchall()
    for number in results:
        x= number[1]
        y= number[0]
        pylab.plot(x,y,'go')
        pylab.show()
 
        
    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])