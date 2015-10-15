# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 23:23:44 2015

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
cursor.execute('select number,num from `user_submit111` ');

rows = cursor.fetchall()

str(rows)[:]
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'number', 1: 'num'}, inplace=True);
df = df.sort(['num'], ascending=[1]);

df.head()

trace1 = Scatter(
    x=df['number'],
    y=df['num'],
    mode='markers'

)
layout = Layout(
    title='用户和提交量的关系',
    xaxis=XAxis( type='log', title='number' ),
    yaxis=YAxis( title='num' ),
)
data = [trace1]
fig = Figure(data=data, layout=layout)
py.plot(data, filename = 'basic-line')

