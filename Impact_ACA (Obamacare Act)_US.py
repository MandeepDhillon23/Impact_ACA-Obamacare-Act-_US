#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Impact of ACA (Obamacare Act) on Health Insuarnce enrollment on US Data 2013-2017 


# In[ ]:


# import plotly
import sys
get_ipython().system('{sys.executable} -m pip install --user plotly')
import plotly


# In[ ]:


import plotly.plotly as py
import pandas as pd

df = pd.read_csv('ACA_data.csv', error_bad_lines=False)


# In[ ]:


# d3-cloropleth-map of USA-States in plotly

import plotly.plotly as py
import pandas as pd
df = pd.read_csv('501data.csv', error_bad_lines=False)
for col in df.columns:
    df[col] = df[col].astype(str)
scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +    ' ACA '+df['ACA']+'<br>'+    'Coverage '+df['Coverage']
   
#df['text']
data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['code'],
        z = df['Coverage'].astype(float),
        locationmode = 'USA-states',
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "In Percent")
        ) ]


layout = dict(
        title = '2017 US Health Insurance Coverage by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
import plotly
plotly.tools.set_credentials_file(username='MandeepDhillon23', api_key='uTRwp5SI5YfOW6ls1LSs')
fig = dict( data=data, layout=layout )
py.iplot( fig, filename='d3-cloropleth-map' )


# In[ ]:


# data on map
trace_1 = go.Scatter(x = df['Year'], y = df['Population(mill)'],
                  name='Population(mill)')
trace_2 = go.Scatter(x = df['Year'], y = df['TotalCoverage(mill)'],
                  name='TotalCoverage(million)')
trace_3= go.Scatter(x = df['Year'], y = df['ACA(mill)'],
                  name='ACA(mill)')
trace_4 = go.Scatter(x = df['Year'], y = df['Income(thou)'],
                  name='Income(thou)')
layout = go.Layout(title='Health Insurance,Population and Income',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)
fig = go.Figure(data=[trace_1,trace_2,trace_3,trace_4], layout=layout)

py.iplot(fig, filename='Health Insurance,Population and Income')


# In[ ]:


# Descriptives of data
import pandas as pd
import numpy as np
df = pd.read_csv("ACA_data.csv")
df.describe()


# In[ ]:


from pandas import stats
df


# In[ ]:


# OLS Regression
import statsmodels.api as sm
model=sm.OLS(Y,X).fit()
model.summary()


# In[ ]:




