import sys 
import pandas as pd
import pathlib

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

markdown_text = '''
### Face Data Information Research Group of Megvii
Xinyu Zhang,Haiwen Huang,Lulu Wang,Sishuo Chen 
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
                                        ["Data Statistics Summary 2016.9-2019.11 树洞历史数据统计总结"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                 children = dcc.Markdown("据不完全统计,从2016年11月到2019年11月,树洞总发帖量952194条,其中删帖12928条,删帖率1.3577%"),
            ),
            dcc.Graph(
                id='year-graph',
                figure={
                    'data': [
                        {'x': [2016,2017,2018,2019], 'y': [83121,186568,245389,424188], 'type': 'bar', 'name': '正常'},
                        {'x': [2016,2017,2018,2019], 'y': [69,2232,4962,5665], 'type': 'bar', 'name': '被删'},
                    ],
                    'layout': {
                        'title': '发帖数量年度走势'
                    }
                }
            ),
            dcc.Graph(
                id='hour-graph',
                figure={
                    'data': [
                        {'x': list(range(0,24)), 'y': [56945,31857,14334,6416,3391,2765,4451,15730,27885,40320,49817,
                        50683,54378,50100,46386,50940,53090,53061,55146,53497,56241,59154,61617,66570], 'type': 'bar', 'name': '发帖数'},
                    ],
                    'layout': {
                        'title': '发帖数量分时走势'
                    }
                }
            ),
            html.Div(
                 children = dcc.Markdown("2016年及之后,回复最多的树洞是[#143790](https://pkuhelper.pku.edu.cn/hole/##143790),爬了2248楼"),
            ),
            html.Img(
                height="432",
                width="768",
                src="https://res.cloudinary.com/dhyonw6zc/image/upload/v1576563507/aca914d9bfbab548642075534abae0b.png",
                className="shot",
            )


    
    ],
    className="page",

    )