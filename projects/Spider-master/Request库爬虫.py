import requests
from bs4 import BeautifulSoup
import json





def gettext(x): 
    return x.get_text()
#设置请求头伪装
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# 先使用requests发送网络请求从而获取网页
html = requests.get('https://movie.douban.com/top250', headers=header)
# print(html.status_code)
# 传入html构建DOM
soup=BeautifulSoup(html.content,'html.parser')
movieNodes = soup.find('ol', attrs={'class': 'grid_view'})
movies=[]
for movie in movieNodes.find_all('li'):
    title=movie.find('div',attrs={'class':'hd'})
    titles=title.find_all('span')
    titles1=map(gettext,titles)
    tit=[]
    for ti in titles1:
      tit.append(ti)
    info=movie.find('p').get_text()
    score=movie.find('span',attrs={'class':'rating_num'}).get_text()
    movies.append({
      "titles": tit,
      "info": info,
      "score": score
    })
f = open("mainpy.json", "w", encoding='utf-8')
json.dump(movies, f, ensure_ascii=False)
f.close()
