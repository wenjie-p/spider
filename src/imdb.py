import requests
import codecs
from bs4 import BeautifulSoup

def get_request_kwargs(timeout, useragent):

    return {
            'headers': {'User-Agent': useragent},
            'timeout': timeout,
            'allow_redirects': True
            }
def get_html(url):

    FAIL_ENCODING = 'ISO-8859-1'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    timeout = 60
    html = ""
    try: 
        print("Starting get html...")
        response = requests.get(url, **get_request_kwargs(timeout, useragent))
        html = response.text
        print("Done with get html...")
    except:
        print("Failed.")
        exit(0)

    return html

def get_soup(url):

    html = get_html(url)
    if html == '':
        print("Get html with empty string")
        exit(0)
    soup = BeautifulSoup(html, 'lxml')
    print("Done with get soup...")

    return soup

def crawl(urls):

    for url in urls:
        soup = get_soup(url)
        print(soup)

if __name__ == "__main__":

    urls = ["https://www.imdb.com/title/tt4154756/reviews?ref_=tt_urv", "https://www.imdb.com/title/tt5690360/reviews?ref_=tt_urv"]

    crawl(urls)
