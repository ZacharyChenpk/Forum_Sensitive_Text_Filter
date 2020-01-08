import dash
import random 
import pickle 
import utils 
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output ,State
import visdcc  
import traceback 
from dash.exceptions import PreventUpdate
import os 
import dash_auth
import time
from dash.exceptions import PreventUpdate 
from utils import *
from text_filter import * 
from pages import (
    Ban,
    About,
    Censoring,
    Search,
    Statistics,
    Contributions,
    Forum 
)
import time 
import string
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

app = dash.Dash()
auth = dash_auth.BasicAuth(
    app,
    {'manager':'pku666'}
)
app.config.suppress_callback_exceptions = True 

pp = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
) 
app.config.suppress_callback_exceptions = True
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/About':
        return  About.create_layout(app)
    if pathname == '/Contributions':
        return  Contributions.create_layout(app)
    if pathname == '/Ban':
        return  Ban.create_layout(app)
    if pathname == '/Statistics':
        return  Statistics.create_layout(app)
    if pathname == '/Forum':
        return  Forum.create_layout(app)
    return Censoring.create_layout(app)

@app.callback(Output("deleted_text","children"),
        [Input("year","value"),Input("month","value"),Input("date","value")])
def update_deleted_holes(year,month,date):
    import os 
    if os.path.exists('deleted/{}-{}-{}.txt'.format(year,month,date)) == False:
        return html.Div("{}-{}-{} 数据暂缺".format(year,month,date))
    fr = open('deleted/{}-{}-{}.txt'.format(year,month,date))
    lines = fr.readlines()
    fr.close()
    return [html.Div(children=line) for line in lines]
@app.callback(Output("operator-led","value"),
              [Input("interval-component", "n_intervals")])
def update_metrics(n):
    
    return time.strftime('%Y:%m:%d:%H:%M:%S',time.localtime(time.time()))

@app.callback(Output("last-update","children"),
              [Input("interval-component", "n_intervals")])
def update_time(n):
    return "上次更新: "+time.strftime('%Y:%m:%d:%H:%M:%S',time.localtime(time.time()))

@app.callback(Output("hour-graph-censoring","figure"),
              [Input("interval-component", "n_intervals")],
              [State("hour-graph-censoring","figure")])
def update_graph(t,figure):
    if t % 180 != 0:
        raise PreventUpdate
    y = figure['data'][0]['y']
    y = y[1:]
    import random 

    y.append(random.randint(0,50))
    return {
                    'data': [
                        {'x': list(range(0,20)), 'y': y, 'type': 'bar', 'name': '发帖数'},
                    ],
                    'layout': {
                        'title': '近一小时发帖数量走势(每三分钟更新一次)'
                    }
                } 


@app.callback(Output("risky_holes","children"),
            [Input("interval-component", "n_intervals")])
def update_risky_holes(t):
    if t == 0 or t % 60 != 0:
        raise PreventUpdate
    
    return gen_riksy_holes_page()

@app.callback(Output("auto_deleted_holes","children"),
            [Input("interval-component", "n_intervals")])
def update_auto_deleted_holes(t):
    if t == 0 or t % 60 != 0:
        raise PreventUpdate
   
    return gen_auto_deleted_holes_page()

def generate_vis_deleted_func():
    def func(n_clicks,pid):
        
        if n_clicks == 0:
            return {'display':'yes'}
        else:
            log = pickle.load(open('demo_log.pkl','rb'))
            log[pid]['censoring_result'] = 3
            pickle.dump(log,open('demo_log.pkl','wb'))
            return {'display':'none'}
    return func 
for i in range(100):
    app.callback(Output('risky_holes_{}'.format(i), 'style'),
                [Input('deletedButton{}'.format(i),'n_clicks')],
                [State('risky_holes_pid{}'.format(i),'children')]
                )(
                    generate_vis_deleted_func() 
                )
                

def generate_vis_auto_deleted_func():
    def func(n_clicks,pid):
        
        if n_clicks == 0:
            return {'display':'yes'}
        else:
            log = pickle.load(open('demo_log.pkl','rb'))
            log[pid]['censoring_result'] = 0
            pickle.dump(log,open('demo_log.pkl','wb'))
            return {'display':'none'}
    return func 
for i in range(100):
    app.callback(Output('auto_deleted_holes_{}'.format(i), 'style'),
                [Input('huifuButton{}'.format(i),'n_clicks')],
                [State('auto_deleted_holes_pid{}'.format(i),'children')]
                )(
                    generate_vis_auto_deleted_func() 
                )

@app.callback(Output('output-label','children'),
            [Input('submit-button','n_clicks')],
            [State('new_input','value')]
)
def suhmit_hole(n_clicks,new_input):
    if n_clicks == 0 :
        raise PreventUpdate 
    censoring_result = sen_detect(new_input)
    time_tag = time.time()
    pid = str(int(round(time.time() * 1000))) + ''.join(random.sample(string.ascii_letters + string.digits, 8))
    new_hole = {'pid':pid,'time':time_tag,'dz_text':new_input,'censoring_result':censoring_result,'replies':[]}
    if os.path.exists('demo_log.pkl'):
        log = pickle.load(open('demo_log.pkl','rb'))
        log[pid] = new_hole
        pickle.dump(log,open('demo_log.pkl','wb'))
    else:
        log = {pid:new_hole}
        pickle.dump(log,open('demo_log.pkl','wb'))
    if censoring_result == 2:
        return "不能发这种坏东西哟"
    if censoring_result == 1:
        return "发布成功！似乎有点奇怪，待会有有人审核哦"
    return "发布成功！"

if __name__ == "__main__":
    server = app.server 
    app.run_server(debug=False,port=8080,host='0.0.0.0')
    