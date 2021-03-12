import requests
import sys
from bs4 import BeautifulSoup     # 网页解析， 获取数据

print("--- 命令行参数:", sys.argv)

api_url = "https://www.gxmu.edu.cn/"
print("--- api_url: ", api_url)

try:
    response = requests.get(api_url)
    #print("--- response headers: ",response.headers)
except requests.exceptions.ConnectionError as e:
 print('Error', e.args)
 exit(1)

html = response.content.decode('gb2312')
# print("--- html: ", html)

soup = BeautifulSoup(html, 'html.parser')   # 将html按照html.parser方式进行解析，然后赋给对象soup

elements = soup.find("div", class_= "mu_content").findChild("div", class_="bd").findChildren("a")
dates = soup.find("div", class_= "mu_content").findChild("div", class_="bd").findChildren("span")
#print("--- element: ", elements)
#print (len(elements), len(dates))

print("--------------- 今日要闻 ---------------")
for i in range (len(elements)):
    print (dates[i].text, elements[i].get('title'))