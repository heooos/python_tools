# -*- coding: utf-8 -*-
import tomd
import requests
import sys
import io
 
reload(sys)
sys.setdefaultencoding("utf8")

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

# 这里填入网址
html_res = requests.get('https://输入需要转换的url', headers=headers)
html_res.encoding = 'utf-8'

# html = """这里是网页内容"""
html = html_res.text

md = tomd.Tomd(html).markdown

# 写入文件 在当前目录下
with io.open('./Title.md', 'wb') as f:
    f.write(md)

f.close()
print("任务已完成")
