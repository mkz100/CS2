

import urllib.request
import urllib.parse

# 1. 获取一个get请求
response = urllib.request.urlopen('http://www.baidu.com')   # 通过urllib.request库里面的urlopen方法打开网页返回数据
print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码   -- response.read()读取方法； .decode('utf-8')是解码



# 2. 获取一个Post请求  -- 必须要传递表单信息
# 封装一个表单信息提交
data = bytes(urllib.parse.urlencode({'hello':'world'}), encoding = 'utf-8')  
'''
bytes()是将所有数据转换成二进制数据包
urllib.parse  解析器
urllib.parse.urlencode({ ：})  封装一个数据， 键值对形式
'''
response = urllib.request.urlopen('http://httpbin.org/post', data = data)
print(response.read().decode('utf-8'))
# *** 总结：
        # 使用post数据访问网页的时候，必须按照post方式访问数据。
        # 怎么封装数据呢？ 就是使用data = data来传递参数



# 3. 超时处理
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
    print(response.read().decode('utf-8'))
except Exception as error:
    print(error)



# 4. 获取状态码
response = urllib.request.urlopen('https://baidu.com')
# print(response.status)      # 获取状态码
print(response.getheaders())    # 得到的是一个列表list


# 伪装成浏览器 -- POST方式
url = 'http://douban.com/post'

# 封装头部信息 -- json形式（字典形式）
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

# 封装data数据
data = bytes(urllib.parse.urlencode({'name':'eric'}), encoding='utf-8')

# 请求对象：req 进行封装处理 -- url=url, data=data, headers=headers, method为那种方法
req = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')    # 封装成一个对象

# 获取请求
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))










# 伪装成浏览器 -- GET方式
url = 'http://douban.com/'
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

req = urllib.re quest.Request(url = url, headers = headers)    # 封装成一个对象
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))