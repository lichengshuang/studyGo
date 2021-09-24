import urllib.request
import urllib.parse
from lxml import etree
import urllib.request
import re

headers = {'User_Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

dict = {'name' : 'zh-CN'}
url = 'http://www.proedu.com.cn/web/shareVideo/index.action?id=1067350&ajax=1'
data = urllib.parse.urlencode(dict).encode('utf-8')
request = urllib.request.Request(url = url, data = data, method = 'GET')
#request.add_header("User-Agent", user_agent)
response = urllib.request.urlopen(request)
#print (response)
html= etree.HTML(response.read())
#print (html)

# //*[@id="title"]
#1 
#result = html.xpath('//*[@id="title"]/text()')
#print (result)
#2
#result1 = html.xpath('//*[@id="my-video_html5_api"]/@src')
#result1 = html.xpath('//*[@id="my-video_html5_api"]/text()')
#result1 = html.xpath('/@src/text()')
#result = html.xpath('//li/a/@href')

result = etree.tostring(html)
#print(result.decode('utf-8'))
a = result.decode('utf-8')

#result = html.xpath('//*[@id="my-video_html5_api"]')
#print (result)
#realAmps = re.match('#Realtime.Amps\=(.*)Amps.*',a)
lines = """
	document.onkeydown=function(event){if(event.keyCode==123){return false;}}&#13;
	var yunxin_player_conf =[{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/Rw6mlJG8_2751657199_shd.mp4","type":"video/mp4"},{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/1v9Tfjon_2751657199_hd.mp4","type":"video/mp4"},{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/G4SCe09F_2751657199_sd.mp4","type":"video/mp4"},{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/c0Pclmch_2751657199_shd.flv","type":"video/x-flv"},{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/wtSX26VP_2751657199_hd.flv","type":"video/x-flv"},{"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/ATkIPcLj_2751657199_sd.flv","type":"video/x-flv"}];&#13;
	var yunxin_player_poster ="http://vod0vwkapu4.nosdn.127.net/87fc343d-e619-4c34-b5ea-228d8fa41e79.jpg";&#13;
	var type="200";&#13;
	var shd ={"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/Rw6mlJG8_2751657199_shd.mp4","type":"video/mp4"};&#13;
	var hd ={"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/1v9Tfjon_2751657199_hd.mp4","type":"video/mp4"};&#13;
	var sd ={"src":"http://vod0vwkapu4.vod.126.net/vod0vwkapu4/G4SCe09F_2751657199_sd.mp4","type":"video/mp4"};&#13;

"""
#print (type(a))
#print (lines)
#for line in lines.split('\n'):
for line in a.split('\n'):
#    print (line)
    #txts = re.match('.*yunxin_player_conf.*=(.*)&#13',a)
    #;&#13
    txts = re.match('\s*var yunxin_player_conf\s=(.*);.*',line)
    if txts:
#        print (txts[1])
        txt = txts[1].split('"')
        print (txt[3])
