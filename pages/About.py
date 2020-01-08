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
                                        ["Motiative 目的"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(children=intro, style={"text-align":"justify"}),
            html.Div(children=chinese_info, style={"text-align":"justify"}),

                        html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Application Background 应用背景"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(children="PKU Hole is a anonymous forum hosted by Peking University for students to communicate freely.Hoevever,improper speeches often lead to severe attacks and privacy disclosure.", style={"text-align":"justify"}),
            html.Div(children="树洞是北大学子自由交流的平台，但不适当的发言经常引起严重争议和隐私泄露", style={"text-align":"justify"}),


            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Implementation 功能实现"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),

            html.Div(
                children = dcc.Markdown('''
                - [x] Improper Text Auto-Detection based on word match and deep learning 基于关键词匹配与深度学习的敏感文本自动识别
                - [x] Auto analysis and log generation about history infomation 历史信息的自动分析和日志生成
                - [x] Automatic censoring and warning 自动监测预警 
                '''),
            ),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Development language 开发语言"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(children="Python,mainly Dash", style={"text-align":"justify"}),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Reference 参考文献"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                children = dcc.Markdown('''
                - [Deep learning for detecting inappropriate content in text](https://link.springer.com/article/10.1007/s41060-017-0088-4)
                -  [Fighting Offensive Language on Social Media with Unsupervised Text Style Transfer](https://arxiv.org/pdf/1805.07685)
                -  [Detecting Hate Speech and Offensive Language on Twitter using Machine Learning: An N-gram and TFIDF based Approach]( https://arxiv.org/abs/1809.08651)
                '''),
            ),
            

    ],
    className="page",

    )