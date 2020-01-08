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
from utils import *
from dash.dependencies import Input, Output 
# get relative data folder

'''
df_dividend = pd.read_csv(DATA_PATH.joinpath("df_dividend.csv"))
df_realized = pd.read_csv(DATA_PATH.joinpath("df_realized.csv"))
df_unrealized = pd.read_csv(DATA_PATH.joinpath("df_unrealized.csv"))
'''

intro = "Improper speeches on various online forums not only seriously affect the user experience, but also may cause operational risks. However, it takes a lot of energy to manually review and delete inappropriate content. In order to solve this problem, we integrate the intelligent filtering model based on natural language understanding into the real web service program, improve the efficiency of sensitive text filtering, and ensure a fresh and healthy communication environment"
chinese_info = "各类网络论坛上的不当发言不但严重影响用户体验，而且还可能发生运营风险，而人工对不当内容进行审查删除需要耗费大量精力。为了探索解决这一困扰网络社区的问题，我们将基于自然语言理解的智能过滤模型整合到真实的Web服务程序中，提高敏感文本过滤的效率，保障清新健康的交流环境"

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
                                        ["发新帖(匿名也要注意文明哦，言论自由是建立在互相尊重的基础上的)"], className="subtitle padded"
                                    ),
                                    
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
             dcc.Input(
                            id="new_input", type="text",
                            style={'width': '100%'},
                            value = "说点什么吧"
            ),
            html.Div(
                children = [
                    
                       
                        html.Div(id='output-label',style={"font-size":"24px",'margin':'30px'}),
                        html.Button(n_clicks=0,id='submit-button', children='确定,发布新帖子',style = {'color':'white','background-color' : '#4CAF50' }),
                ],
                style = {'text-align':'center'}
            ),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["最近帖子"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                id = 'forum_demo',
                children = read_pages() 
                
            ),
            

    ],
    className="page",

    )