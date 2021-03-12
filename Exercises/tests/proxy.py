import requests,random

#定义代理池
proxy_list = [
 '191.101.39.238',
]

# 随机选择一个代理
proxy = random.choice(proxy_list)

proxies = {
 'http': 'http://' + proxy,
 'https': 'https://' + proxy,
}
try:
 response = requests.get('http://httpbin.org/get', proxies=proxies)
 print(response.text)
except requests.exceptions.ConnectionError as e:
 print('Error', e.args)
