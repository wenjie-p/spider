import requests
from urllib import urlretrieve
from bs4 import BeautifulSoup
import codecs
from PIL import Image
from os import remove
import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")

def spider(f,url,doc):
    print url
    html = f.get(url).text
    soup = BeautifulSoup(html,"lxml")
    tag = soup.select("#comments")[0]
    doc.append(url)
    for p in tag.select("p"):
        for comment in p.stripped_strings:
            print comment
if __name__ == "__main__":

    doc = []

    with requests.Session() as c:
        url  = "https://accounts.douban.com/login?source=movie"
        form_email = ""
        form_passwd = ""
        #page = c.post(url).text
        #soup = BeautifulSoup(page, "html.parser")
        
        '''
        img_src = soup.find('img',{"id":"captcha_image"}).get("src")
        urlretrieve(img_src, "captcha.jpg")
        try:
            im = Image.open("captcha.jpg")
            im.show()
            im.close()
        except:
            print "open the local path"

        finally:
            captcha = raw_input("please input the captcha:")
            remove("captcha.jpg")

        captcha_id = soup.find("input",{"type":"hidden", "name":"captcha-id"}).get("value")
        '''
        login_data = dict(form_email = form_email, form_password = form_passwd)
        #login_data["captcha-id"] = captcha_id
        #login_data["captcha-solution"] = captcha
        c.post(url, data = login_data, headers = {"Referer":"https://accounts.douban.com/login?source=movie"})
        url = "https://movie.douban.com/subject/27115344/comments?start={}&limit=20&sort=new_score&status=P&percent_type="
        for i in range(170):
            sub_url = url.format(i * 20)
            spider(c,sub_url,doc)
        '''
        f = codecs.open("comments", "w", encoding = "utf8")
        for line in doc:
            f.write(line + "\n")
        f.close()
        '''
