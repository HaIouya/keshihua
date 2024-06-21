from flask import Flask, render_template,request
import jieba
import pandas as pd
import json
import numpy as np
import seaborn as sns
import warnings
import os
from collections import Counter
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Grid, Line, Pie, Tab,Map,Page, WordCloud
from picture import mpg_view,vbar,wordcloud,xueli,beijing,shanghai,guangzhou


app = Flask(__name__)

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 项目页1-招聘岗位数量页
@app.route('/mpg')
def xiangmu():
    with open("templates/mpg.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())
    with open("templates/vbar.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())
    return render_template('base.html',
                           the_plot_all1 = plot_all1,the_plot_all2 = plot_all2)

# 项目页2-北上广具体市区招聘岗位数量情况页
@app.route('/fenqu')
def fenqu():
    with open("templates/beijing.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

        return render_template(
            "base3.html",the_plot_all1 = plot_all1
            )   

@app.route('/gz_fenqu')
def gz_fenqu():
    with open("templates/guangzhou.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

        return render_template(
            "base3.html",the_plot_all1 = plot_all1
            )   

@app.route('/sh_fenqu')
def sh():
    with open("templates/shanghai.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

        return render_template(
            "base3.html",the_plot_all1 = plot_all1
            )   


# 项目页3-词云图页
@app.route('/wordcloud')
def ciyun():
    with open("templates/wordcloud.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())
    return render_template('base2.html',
                           the_plot_all1 = plot_all1)

# 项目页4-岗位要求页
@app.route('/experience')
def yaoqiu():
    with open("templates/xueli.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())
    with open("templates/jingyan.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())
    return render_template('base4.html',
                           the_plot_all1 = plot_all1,the_plot_all2 = plot_all2)


# 项目页5-公司页
@app.route('/company')
def leixing():
    with open("templates/leixing.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())
    with open("templates/leixing2.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())
    return render_template('base5.html',
                           the_plot_all1 = plot_all1,the_plot_all2 = plot_all2)



if __name__ == '__main__':
    app.run()
