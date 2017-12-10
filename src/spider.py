#Author: yuebanyishenqiu
#E-mail:thisispwj@outlook.com
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import requests
from bs4 import BeautifulSoup
import codecs
import time
def get_request_kwargs(timeout,useragent):
    #add some parameters
    return{
        'headers':{'User-Agent':useragent},
        'timeout':timeout,
        'allow_redirects':True
    }

def getHtml(url):
    FAIL_ENCODING = 'ISO-8859-1'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    timeout = 7
    try:
        print url
        response=requests.get(url,**get_request_kwargs(timeout,useragent))
        if response.encoding!=FAIL_ENCODING:
            html = response.text
        else:
            html=response.content
        if html is None:
            return u''
        return html
    except:
        return u''
def getSoup(url):
    html=getHtml(url)
    if html==u'':
        return None
    soup=BeautifulSoup(html,'lxml')
    return soup
def getSubUrls(url):
    soup=getSoup(url)
    if soup is None:
        print "Error"
        return 
    tags=[x for x in soup.find_all(attrs={"data-role":"news-item"})]#if x not in soup.find_all(attrs={"data-god-id":re.compile("\d+")})]
    for tag in tags:
        child=tag.select("h4 > a")
        link=child[0].get('href')
        if link is not None:
            if url not in link:
                link="http:"+link
            yield link
def spider(url):
    i = 0
    for suburl in getSubUrls(url):
        soup=getSoup(suburl)
        title_tag = soup.find('h1')
        t_stamp = time.time()
        st = time.localtime(t_stamp)
        t_str = time.strftime("%Y-%m-%d",st)
        for title in title_tag.stripped_strings:
            f = codecs.open('../data/' + t_str + "_" + str(i),'w',encoding="utf8")
        article = soup.find('article')
        for para in article.stripped_strings:
            f.writelines(para+'\n')
        f.close()
        i += 1
if __name__=="__main__":
    spider('http://business.sohu.com/')
