# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:29:09 2015

@author: melo
"""

import pylab
values=[944545,5893810]
pieLabels=['others','top 2w']
colorLst=('r','g')
pylab.pie(values,labels=pieLabels,colors=colorLst)
pylab.title('Pie chart of sum of submit')
pylab.show()