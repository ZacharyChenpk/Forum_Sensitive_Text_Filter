import sys 
import pandas as pd
import pathlib
from tqdm import tqdm
from utils import Header, make_dash_table  
from utils import encoded_image 
import base64 
import dash
import random 
import pickle
import dash_core_components as dcc
import dash_html_components as html 

from dash.dependencies import Input, Output 
# get relative data folder

'''
df_dividend = pd.read_csv(DATA_PATH.joinpath("df_dividend.csv"))
df_realized = pd.read_csv(DATA_PATH.joinpath("df_realized.csv"))
df_unrealized = pd.read_csv(DATA_PATH.joinpath("df_unrealized.csv"))
'''


def create_layout(app):
    fr = open('deleted/2018-1-1.txt')
    lines = fr.readlines()
    fr.close()
    return html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Deleted Holes 被删树洞迷惑行为大赏"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                 children = dcc.Markdown("2016年11月8日到2019年11月24日数据，仅供北大同学研究参考，请勿外传造成社会影响"),
            ),
            html.Div( id = 'setting-UI',
        children = [
            html.Div(
                children = [
                    html.Label('Year 年份',style={'color':'blue'}),
                        dcc.Dropdown(
                            id = 'year',
                            options=[ 
                                {'label': str(i), 'value': i} for i in range(2016,2020)],
                            value=2018,
                            
                        ),
                ],
                style={'width': '33%', 'display': 'inline-block'}
            ) , 
            
            html.Div(
                children = [
                    html.Label('Month 月份',style={'color':'blue'}),
                    dcc.Dropdown(
                        id = 'month',
                        options=[{'label':i,'value':i} for i in range(1,13)
                        ],
                        value=1,
                          
                    ),
                ] ,
                style={'width': '33%', 'display': 'inline-block'}
            ) ,
            html.Div(
                children = [
                    html.Label('Date 日期',style={'color':'blue'}),
                    dcc.Dropdown(
                        id = 'date',
                        options=[{'label':i,'value':i} for i in range(1,32)
                        ],
                        value=1,
                          
                    ),
                ] ,
                style={'width': '33%', 'display': 'inline-block'}
            ) ,

        ],


    ),
    html.Div(
        id = 'deleted_text',
        children = [html.Div(children = line) for line in lines]
    )
    
    ]
    )