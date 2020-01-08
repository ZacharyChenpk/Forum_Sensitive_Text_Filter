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
                                        ["Search 搜索"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                 children = "输入关键词进行搜索(结果包含已被官方删除部分)",
            ),
            html.Div(
                children=[
            
                # dcc.Markdown(markdown_text),

                    html.Label('输入关键词',style={'color':'blue'}),
                    dcc.Input(id='keyword',value='email', type='text'), 
                    #html.Div(id='output_name'),
                    html.Label('input',style={'color':'blue'}),
                    dcc.Input(id='input',value='关键词', type='text'), 
                    html.Button(id='signup_button',n_clicks=0,children='搜索',
                    style = {'color':'white','background-color' : '#4CAF50' }),
                    
                ],
                style={'columnCount': 2}
        
            ),

    
    ],
    className="page",

    )