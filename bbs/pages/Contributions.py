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
Sishuo Chen,Junior Student from Peking University  

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
                                        ["Developer 开发者"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(children='''Sishuo Chen,Junior Student at Peking University'''),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Contact 联系"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                 children = dcc.Markdown("[chensishuo@pku.edu.cn](mailto:chensishuo@pku.edu.cn)"),
            ),
            html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Acknowledgement 鸣谢"], className="subtitle padded"
                                    ),
                                   
                                    
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
            ),
            html.Div(
                 children = dcc.Markdown('''
                 感谢北京大学校园应用[PKU Helper](https://pkuhelper.pku.edu.cn/)的开发团队，以及2019年秋季计算机网络与Web技术的指导老师 [张岩](https://eecs.pku.edu.cn/info/1342/6102.htm) 教授。
                 
                 - The Development team of the campus APP [PKU Helper](https://pkuhelper.pku.edu.cn/)
                 - The Director of the Computer Network and Web Techology course in PKU [Yan Zhang](https://eecs.pku.edu.cn/info/1342/6102.htm)
                 
                 '''),
            ),
    
    ],
    className="page",

    )