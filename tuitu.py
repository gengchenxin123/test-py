# 学习人：耿晨鑫
# 时间：2022/12/7
import time
import re
import os
from lxml import etree
import  requests

url_base='https://www.tuiimg.com/meinv/'
header={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
os.makedirs('./tuitu',exist_ok=True)
os.makedirs('./tuitu/img',exist_ok=True)
resp=requests.get(url_base,header)
# print(resp.text)
num=1
for i in range(1,10):
    if i==1:
        url_base = f'https://www.tuiimg.com/meinv/list_{i}.html'
        resp = requests.get(url_base, header)
        time.sleep(3)
        # '<li><a href="(.*?)" class="pic" target="_blank">'
        pattern='<li><a href="(.*?)" class="pic" target="_blank"><img src=".*?"  alt=".*?" /></a><a href=".*?" class="title" target="_blank">.*?</a></li>'
        img_result=re.findall(pattern,resp.text)

        # print(img_result)
        for j in range(len(img_result)):
            url_detail=img_result[j]
            res_detail=requests.get(url_detail,header)
            # print(url_detail)
            res_detail.encoding='utf-8'
            time.sleep(2)
            # result=res_detail.text
            root=etree.HTML(res_detail.text)
            img_url=root.xpath('// *[ @ id = "nowimg"]/@src')
            # res=img_url.split[-1:-4:1]
            # print(res)
            for x in img_url:
                print(x)
                print(f"正在下载低{i}页的第{num}张图片")
            time.sleep(2)
            img_data=requests.get(x,header).content
            time.sleep(1)
            with open(f'./tuitu/img/{num}.jpg','wb') as f:
                f.write(img_data)
            num=num+1
    else:
        url_base = f'https://www.tuiimg.com/meinv/list_{i}.html'
        resp = requests.get(url_base, header)
        time.sleep(3)
        # '<li><a href="(.*?)" class="pic" target="_blank">'
        pattern='<li><a href="(.*?)" class="pic" target="_blank"><img src=".*?"  alt=".*?" /></a><a href=".*?" class="title" target="_blank">.*?</a></li>'
        img_result=re.findall(pattern,resp.text)

        # print(img_result)
        for j in range(len(img_result)):
            url_detail=img_result[j]
            res_detail=requests.get(url_detail,header)
            # print(url_detail)
            res_detail.encoding='utf-8'
            time.sleep(2)
            # result=res_detail.text
            root=etree.HTML(res_detail.text)
            img_url=root.xpath('// *[ @ id = "nowimg"]/@src')

            # print(img_url)
            for x in img_url:

                print(f"正在下载低{i}页的第{num}张图片")
            time.sleep(2)
            img_data=requests.get(x,header).content
            time.sleep(1)
            with open(f'./tuitu/img/{num}.jpg','wb') as f:
                f.write(img_data)
            num=num+1
