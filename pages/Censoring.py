import sys 
import pandas as pd
import pathlib
import time 
from utils import Header, make_dash_table  
from utils import encoded_image 
import base64 
import dash
import random 
from utils import *
import pickle
import dash_core_components as dcc
import dash_html_components as html 
import dash_daq as daq
from dash.dependencies import Input, Output 
# get relative data folder

'''
df_dividend = pd.read_csv(DATA_PATH.joinpath("df_dividend.csv"))
df_realized = pd.read_csv(DATA_PATH.joinpath("df_realized.csv"))
df_unrealized = pd.read_csv(DATA_PATH.joinpath("df_unrealized.csv"))
'''


def create_layout(app):
    
    return html.Div(
        [
            Header(app),
            # page 5
           
           

            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Monitor 实时分析预警"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(id = 'last-update',children="Last Update: "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))),
            html.Div(
                id="card-1",
                children=[
                    daq.LEDDisplay(
                        id="operator-led",
                        value=time.strftime('%Y:%m:%d:%H:%M:%S',time.localtime(time.time())),
                        color="#92e0d3",
                        backgroundColor="#1e2130",
                        size=60,
                    ),
                ],
            ),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["当前发贴量平稳,未见热点爆发"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            dcc.Graph(
                id='hour-graph-censoring',
                figure={
                    'data': [
                        {'x': list(range(0,24)), 'y': [56,31,14,64,33,27,44,15,27,40,49,
                        50,54,50,46,50,53,53,55,53,23,34,23,2], 'type': 'bar', 'name': '发帖数'},
                    ],
                    'layout': {
                        'title': '近24小时发帖数量走势'
                    }
                }
            ),
            dcc.Graph(
                id='year-graph-censoring',
                figure={
                    'data': [
                        {'x': list(range(1,31))[::-1], 'y': [i*24 for i in [56,31,14,64,33,27,44,15,27,40,49,
                        50,54,50,46,50,53,53,55,53,23,45,56,32,45,34,56,73,45,21]], 'type': 'bar', 'name': '发帖数'},
                    ],
                    'layout': {
                        'title': '近一个月发帖数量走势(距今x天)'
                    }
                }
            ),
           html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["近期高风险帖子核查（每分钟更新一次）"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                id = 'risky_holes',
                children = gen_riksy_holes_page() 
                
            ),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["近期自动删除帖子恢复审核(每分钟更新一次)"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                id = 'auto_deleted_holes',
                children = gen_auto_deleted_holes_page() 
                
            ),
            
                        html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["近期高频话题分析(近五天)"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                            html.Img(
                                height="616",
                                width="784",
                                src="https://res.cloudinary.com/dhyonw6zc/image/upload/v1577962819/0952ea97c9a04c1475149f6d8b8ec4c.png",
                                className="wordcloud",
                        
                            ),
                        ],
                        className="row ",
            ),
    
    ],
    className="page",

    )