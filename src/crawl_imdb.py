import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/title/tt0371746/reviews?ref_=tt_urv'
res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")

main_content = urljoin(url,soup.select(".load-more-data")[0]['data-ajaxurl'])  ##extracting the link leading to the page containing everything available here
response = requests.get(main_content)
broth = BeautifulSoup(response.text,"lxml")

for item in broth.select(".review-container"):
    title = item.select(".title")[0].text
    review = item.select(".text")[0].text
    print("Title: {}\n\nReview: {}\n\n".format(title,review))
