# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 20:32:46 2015

@author: melo
"""


import MySQLdb
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("melo", "muu68y1g1d")
conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
cursor = conn.cursor()
conn.select_db('phpmyadmin')
cursor.execute('select time,times from `user_time22` ');

rows = cursor.fetchall()

str(rows)[:]
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'time', 1: 'times'}, inplace=True);
df = df.sort(['time'], ascending=[1]);

df.head()

trace1 = Scatter(
    x=df['time'],
    y=df['times'],
    mode='markers'

)
layout = Layout(
    title='时间和提交量的关系',
    xaxis=XAxis( type='log', title='time' ),
    yaxis=YAxis( title='times' ),
)
data = [trace1]
fig = Figure(data=data, layout=layout)
py.plot(data, filename = 'basic-line')

