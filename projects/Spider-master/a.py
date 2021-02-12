import urllib.request

# 伪装成浏览器 -- GET方式
url = 'http://douban.com/'
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

req = urllib.request.Request(url = url, headers = headers)    # 封装成一个对象
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))