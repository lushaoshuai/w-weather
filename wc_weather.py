import requests
from time import ctime
from bs4 import BeautifulSoup
import itchat
def getPM25(cityname):
    site='http://www.pm25.com/'+cityname+'.html'
    r=requests.get(site)
    soup=BeautifulSoup(r.text,'lxml')
    city=soup.find(class_='bi_loaction_city')
    aqi=soup.find(class_='bi_aqiarea_num').get_text()
    result=soup.find(class_='bi_aqiarea_bottom').get_text()
    quality=soup.select(".bi_aqiarea_right span")
    '''
    不同空气等级对应不同的类名，应用find
    class_='bi_aqiarea_wuran wuranlevel_1'or 'bi_aqiarea_wuran wuranlevel_2 '
    '''
    print(quality)
    output=cityname+'\n'+u'AQI指数:'+aqi+u'\n空气质量状况：'+quality[0].text+result
    return output
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    if msg['ToUserName']!='filehelper':
        return
    cityname=msg['Text']
    response=getPM25(cityname)
    itchat.send(response,'filehelper')
itchat.auto_login(hotReload=True)
Help='请输入城市拼音获取天气结果，如果无法识别，自动返回首都记录'
itchat.send(Help,'filehelper')
itchat.run()
