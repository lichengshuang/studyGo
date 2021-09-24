#!/usr/bin/python3

"""
2021 09 23 
一个比较好的go语言视频教程
书本上有二维码看视频
通过比较不同二维码的url的关系发现 一本书的视频是连续的
再通过url 发现 这个视频是可以通过一些手段给拿到地址 从而把他给下载下来
"""

import configparser
import shutil
import base64
###随机生成客户端
from userAgent import UserAgent

import json



##爬去网站相关的模块
import urllib.request
import urllib.parse
from lxml import etree
from bs4 import BeautifulSoup
import logging

import time
import os
import sys
import random
import datetime
import logging


logger = logging.getLogger('log')

starttime = datetime.datetime.now()
FORMAT = '%(asctime)-15s %(levelname)s  %(filename)s[line:%(lineno)d]  %(message)s'
LOGFILE = "/var/log/govedio." + time.strftime("%Y%m%d") + '.log'
logging.basicConfig(filename=LOGFILE, level=logging.INFO,format=FORMAT)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

###客户端
##这里替换成一个大文件了

def getConfig():
    global fileName, basePath, confPath 
    global FilesPath, mp4path, userUrl

    global musicfile
    ##musicfile 定义歌的文件目录地址

    ##脚本名
    fileName = os.path.abspath(__file__)
    ##脚本的上一级目录 离开bin目录
    binPath = os.path.dirname(os.path.realpath(__file__))
    basePath = os.path.dirname(binPath)
    ##
    #配置文件的目录
    confPath = basePath + '/config/'

    conf = configparser.ConfigParser()
    conf.read("%s/config.ini" % confPath)
    #logging.info ("%s/config.ini" % confPath)
    ##放歌曲的目录,用于通过歌曲名字去下载简谱
#    userUrl = conf.get('globle','userUrl')
    ##放简谱图片的文件
    mp4path = conf.get('globle','mp4path')
    #mp4path = '/export/createvhost/music/j简谱/'

def getUrlContent(xpaths,url):
    """
        xpaths 用xpath来提取url文件
        User-Agent
    """
    #user_agent = random.choice(ua_list)
    user_agent = UserAgent()
    headers = {'User_Agent' : user_agent}
    dict = {'name' : 'zh-CN'}
    data = urllib.parse.urlencode(dict).encode('utf-8')
    request = urllib.request.Request(url = url, data = data, method = 'GET')
    request.add_header("User-Agent", user_agent)
    response = urllib.request.urlopen(request)
    html= etree.HTML(response.read())
    aresults = html.xpath('%s' % xpaths)
    logging.info(aresults)
    #logging.info ('%s' % aresults)
    return aresults

def getUrlmv(url):
    import re
    user_agent = UserAgent()
    headers = {'User_Agent' : user_agent}
    dict = {'name' : 'zh-CN'}
    data = urllib.parse.urlencode(dict).encode('utf-8')
    request = urllib.request.Request(url = url, data = data, method = 'GET')
    request.add_header("User-Agent", user_agent)
    response = urllib.request.urlopen(request)
    html= etree.HTML(response.read())
    result = etree.tostring(html)
    #logging.info(result.decode('utf-8'))
    ## 通过xpath 没有获取到视频的url,只能通过这个方法搞一下

    a = result.decode('utf-8')
    for line in a.split('\n'):
        ##通过re 查找url
        txts = re.match('\s*var yunxin_player_conf\s=(.*);.*',line)
        if txts:
    #        logging.info (txts[1])
            txt = txts[1].split('"')
            mp4url = (txt[3])
            logging.info (mp4url)
            return mp4url

def xiazaimv(mp4path,mp4url,filename):
    ##简谱存放目录文件名
    #res = sooopuDownloadPic(aurl,songpath2,pngname)
    user_agent = UserAgent()
    name = mp4path + '/' + str(filename)  +  '.mp4'
    ###下载处理headers
    if os.path.exists(name):
        logger.info('文件已存在: %s ' % name)
        return name
    opener = urllib.request.build_opener()
    opener.addheaders =[("User-Agent", user_agent)]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(mp4url,name)
        #logging.info ('%s下载ok!\n' % pngname)
        ##返回简谱的目录地址
        return name
    except Exception as e:
        logging.info ('e')
        logging.info ('%s没有下到\n' % name)
        return None

                      
    

def main(url):

    ##
    try:
        targetnamegs='//*[@id="title"]/text()'
        ## 获取视频的标题
        infoJianPuxin = getUrlContent(targetnamegs,url)
        filename = infoJianPuxin[0].strip('\'')
        logging.info (filename)
        ## 获取视频的地址
        mp4url = getUrlmv(url)

        #songdicts = {}
        ## 下载
        if mp4url:
            res = xiazaimv(mp4path,mp4url,filename)
            if res:
                songdicts[filename] = {}
                songdicts[filename]['name'] = filename
                songdicts[filename]['url'] = url
                songdicts[filename]['mp4url'] = mp4url
                songdicts[filename]['localpath'] = res
    except Exception as e:
        logging.info (e)


if __name__ == '__main__':
    ###对于下载结果做一个收集
    getConfig()
    ##以下几行是把歌曲的信息存起来
    #每次读取 假如已经有了就不再继续抓取了
    ##
    global songdicts
    songdicts = {}
    songdictfile = '%s/vedioinfo.json' % (basePath)
    try:
        with open(songdictfile,'r') as f:
            songdicts = json.loads(f.read())
    except Exception as e:
        logging.info (e)
        songdicts = {}

    allusrs = []
    with open('url.txt', 'r') as f:
        for line in f.readlines():
            url = line.strip()
            #print (url)
            logging.info (url)
            main(url)


    line = json.dumps(songdicts,sort_keys=False,indent=4,ensure_ascii=False) + "\n"
    with open('%s/vedioinfo.json' % basePath,'w') as f:
        f.write(line)
    #logging.info(aresults)
