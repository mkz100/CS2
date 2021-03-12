import random
import requests
import sys
from bs4 import BeautifulSoup     # 网页解析， 获取数据

print("--- 命令行参数:", sys.argv)
# print(len(sys.argv) )
if len(sys.argv) < 2:
    # expect 2 arguments: cmd, 城市名
    print(f"用法: {sys.argv[0]} 城市名")
    exit(1)

# get the URL you want to shorten from cmd line
city_name = sys.argv[1]

# https://www.chahaoba.com/南宁
api_url = f"https://www.chahaoba.com/{city_name}"
print("--- api_url: ", api_url)

#定义代理池
proxy_list = [
    '191.101.39.238',
    '191.101.39.27',
    '161.202.226.194'
]

# 抱歉，系统检测到您的访问过于密集，暂时进行了ip屏蔽，如有疑问请联系：webmaster@chahaoba.com
# 随机选择一个代理
proxy = random.choice(proxy_list)

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}

ramdon_ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
#ramdon_ip = "89.0.1.0"
request_headers = {"User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ramdon_ip} Safari/537.36"}
print("--- request headers: ", request_headers)

# s = requests.session()
# s.proxies = proxies

# make the request
try:
    response = requests.get(api_url, headers=request_headers)
    #response = requests.get(api_url, headers=request_headers, proxies=proxies)
    #s.get(api_url)

    print("--- response headers: ",response.headers)

    print("--- response: ", response.text)

except requests.exceptions.ConnectionError as e:
 print('Error', e.args)


