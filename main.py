import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%ED%8C%8C%EC%9D%B4%EC%8D%AC&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=&fromage=any&limit=20&sort=&psf=advsrch&from=advancedsearch"
)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")
spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[0:-1])