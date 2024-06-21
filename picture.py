from bokeh.plotting import figure
from pyecharts.charts import Bar, Grid, Line, Pie, Tab
import jieba
import pandas as pd
from collections import Counter
from pyecharts.charts import Line,Pie,Scatter,Bar,Map,Grid
from pyecharts.charts import WordCloud
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Funnel
import os
import numpy as np
import pyecharts.options as opts


df = pd.read_excel('data/2022年数据分析岗位招聘数据.xlsx')

df['城市'] = df['地点'].apply(lambda x:x.split('-')[0])

#滑动柱状图
def mpg_view():
    job_demand = df.省份.value_counts().sort_values(ascending=True)
    color_js = """new echarts.graphic.LinearGradient(0, 0, 1, 0,
        [{offset: 0, color: '#72EDF2'}, {offset: 1, color: '#5151E5'}], false)"""
    x_data = job_demand.index.tolist()
    y_data = job_demand.values.tolist()
    b1 = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('',
                       y_data,
                       category_gap="50%",
                       label_opts=opts.LabelOpts(
                           position='top',
                           font_size=13,
                           color='#333333',
                           font_weight='bolder',  
                           font_style='normal',  
                           formatter='{c}'
                       ),
                       )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(color_js),
                    "barBorderRadius": [100, 100, 100, 100]
                }
            }
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title='数据分析岗位招聘数量省份排名',
                                      title_textstyle_opts=opts.TextStyleOpts(),
                                      pos_top='7%', pos_left='center'
                                      ),
            legend_opts=opts.LegendOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            yaxis_opts=opts.AxisOpts(name="",
                                     name_location='middle',
                                     name_gap=40,
                                     name_textstyle_opts=opts.TextStyleOpts(font_size=16)),
            datazoom_opts=[opts.DataZoomOpts(range_start=1, range_end=50)]
        )

    )

    b1.render('templates/mpg.html')

#地图
def vbar():
    df_city=df['省份'].value_counts()
    m1 = (
        Map()
            .add('全国数据分析岗位数量分布', [list(z) for z in zip(df_city.index.values.tolist(), df_city.values.tolist())],
                 'china')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='全国数据分析岗位数量分布'),

            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=False,
                                              range_color=["white", "#72EDF2", "#5151E5"]),
        )
    )
    m1.render('templates/vbar.html')


#词云图
def wordcloud():
    tag_array = df['岗位标签'].apply(lambda x:eval(x)).tolist()
    tag_lis = []
    for tag in tag_array:
        tag_lis += tag
    tag_df = pd.DataFrame(tag_lis,columns = ['职位标签'])
    tag_df_cnt = tag_df['职位标签'].value_counts().reset_index()
    tag_df_cnt.columns = ['职位标签','计数']
    word_cnt_lis = [tag for tag in zip(tag_df_cnt['职位标签'],tag_df_cnt['计数'])]

    wc = (
        WordCloud()
            .add("",
                 word_cnt_lis,
                 shape="diamond"
                 )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="数据分析岗位标签词云图"),

        )

    )
    wc.render('templates/wordcloud.html')


#环形图
def xueli():
    g = df2.groupby('学历要求')
    job_name =  g.count()['职位名称']
    directions = job_name.index.tolist()
    count = job_name.values.tolist()

    c1 = (
    Pie(init_opts=opts.InitOpts())
        .add(
        '',
        [list(z) for z in zip(directions, count)],
        radius=['40%', '75%'],
        center=['40%', '50%'],
#         rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True),
                    itemstyle_opts={
            "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    'shadowBlur': 10,
                    'shadowColor': 'rgba(0,191,255,0.5)',
                    'shadowOffsetY': 1,
                    'opacity': 0.8,
                
                    }
                       },
        )    
        .set_global_opts(
            title_opts=opts.TitleOpts(title='学历要求',
                                      pos_left='1%'
                                     ),
             legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%",pos_top="25%",orient="vertical")
                        )
                .set_series_opts(
            abel_opts=opts.LabelOpts(
                formatter="{b}：{d}%",
                color="#00c6d7",
                font_size="20",
                
            ),
        )
    )
    c1.render('templates/xueli.html')





def echarts_bar(x,y,title = '主标题',subtitle = '副标题',label = '图例'):
    bar = Bar(
            init_opts=opts.InitOpts(
            theme='shine', 

        )
    )
    bar.add_xaxis(job_experience.index.tolist())
    bar.add_yaxis(label,job_experience.values.tolist(),
        label_opts=opts.LabelOpts(is_show=True) 
        ,category_gap="50%"
        ) 
    bar.reversal_axis()
    bar.set_series_opts( 
        label_opts=opts.LabelOpts(
            is_show=True,
            position='right', 
            font_size=15,
            color= '#333333',
            font_weight = 'bolder',  
            font_style = 'oblique',  
            ), 
        itemstyle_opts={  
            "normal": {
                "color": JsCode(
                   """new echarts.graphic.LinearGradient(0, 0, 1, 0,
    [{offset: 0, color: '#72EDF2'}, {offset: 1, color: '#5151E5'}], false)"""
                ),       # 调整柱子颜色渐变
                'shadowBlur': 6,   # 光影大小
                "barBorderRadius": [100, 100, 100, 100],  # 调整柱子圆角弧度
                "shadowColor": "#999999", # 调整阴影颜色
                'shadowOffsetY': 2,
                'shadowOffsetX': 2,  # 偏移量
            }
        }
    )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title=title, 
            subtitle=subtitle, 

            title_textstyle_opts=opts.TextStyleOpts(color='#2C3B4C', font_size=20,font_weight='bolder')
        ),
        legend_opts=opts.LegendOpts(
            is_show=True, 
            pos_left='right', 
            pos_top='3%',  
            orient='horizontal'  
        ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True,  
            trigger='axis',  
            trigger_on='mousemove|click',  
            axis_pointer_type='cross',  
        ),
        yaxis_opts=opts.AxisOpts(
            is_show=True,
            splitline_opts=opts.SplitLineOpts(is_show=False), 
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(  
                font_size=13,  
                font_weight='bolder' 
            ),
        ),   
        xaxis_opts=opts.AxisOpts(
            boundary_gap=True,   
            axistick_opts=opts.AxisTickOpts(is_show=True),  
            splitline_opts=opts.SplitLineOpts(is_show=False), 
            axisline_opts=opts.AxisLineOpts(is_show=True),  
            axislabel_opts=opts.LabelOpts(  
                font_size=13,  
                font_weight='bolder' 
            ),
        ),
    )
    bar.render('templates/jingyan.html')



#柱状图
def beijing():
  beijing_demand = df[df['城市'] == '北京']['地点'].value_counts().sort_values(ascending = False)
  c1 = (
    Bar()
    .add_xaxis(beijing_demand.index.tolist())
    .add_yaxis("岗位数", beijing_demand.values.tolist(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="北京市各个地区岗位分布数量情况"))

)
  c1.render('templates/beijing.html')




def shanghai():
  shanghai_demand = df[df['城市'] == '上海']['地点'].value_counts().sort_values(ascending = False)
  c2 = (
    Bar()
    .add_xaxis(shanghai_demand.index.tolist())
    .add_yaxis("岗位数", shanghai_demand.values.tolist(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="上海市各个地区岗位分布数量情况"))

)
  c2.render('templates/shanghai.html')



def guangzhou():
  guangzhou_demand = df[df['城市'] == '广州']['地点'].value_counts().sort_values(ascending = False)
  c3 = (
    Bar()
    .add_xaxis(guangzhou_demand.index.tolist())
    .add_yaxis("岗位数", guangzhou_demand.values.tolist(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="广州市各个地区岗位分布数量情况"))

)
  c3.render('templates/guangzhou.html')