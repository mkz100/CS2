# 用Python来实现缩短网址服务

## 重要概念

我们通过这个项目来学习加强对这些概念的理解:

1. 什么是API
2. 什么是 WEB API
3. 什么是 REST API
4. 为什么 API 非常重要? 
5. 什么是HTTP? 他最常用的两个请求方法(methods)是什么? 
6. HTTP 和 REST API 是什么关系? 
   
* 程序接口(API)就像空气和水一样，已经渗透到你们生活学习中的每一个角落。比如你们的手机上所有的App包括微信都是通过API和后面的服务器进行对话。
* 每一个网址其实都是一个 REST API. REST API 是最常见应用最广泛的 WEB API。 
* 每一个网页的浏览, 都是一个HTTP请求. 每一个HTTP请求都是调用一个 REST API. 
* 离开了 WEB API, 你寸步难行: 不能网上购物，不能网上转账，不能发微信, 不能打车出行...

知道这些概念以后， 这个项目就很容易理解, 也很有实际意义。


## 项目背景和使用场景
1. 大家很可能都遇到过: 要分享的网址很长, 放到社交媒体(微博,微信)上不方便, 怎么办? 
2. 有些程序或者网站需要提供缩短网址的服务, 比如 Twitter 和微博不能超过140个字符。 

比如: 你有这样一个网址: 太长，不好记, 不好分享 --
https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978

你肯定想把它缩短成一个好记的网址。
你有两种做法:
1. 到提供该服务的网站上去, 人工输入你的网址，然后让这个网站给你缩短你的网址。 
2. 调用服务网站提供都API, 自己编程的方法来实现。 
   
如果你要大量处理，或者在程序中来获取这个服务, 那编程来实现是你唯一的选择。 


## 调用第三方 WEB API 来实现缩短网址服务

搜索一下就发现有好多网站提供这样的服务。我们今天来一起探讨一下两个比较常见的网站 --
1. cutt.ly
2. bit.ly

### Cutt.ly 网站和API

1. 注册
2. 查阅API 文档: https://cutt.ly/api-documentation/cuttly-links-api
3. API Key: e77a2e10762f46d8be84d47974d4703310301
4. Python 四部分:
   1. 获取参数
   2. 构建REST API URL: `--- api_url:  https://cutt.ly/api/api.php?key=e77a2e10762f46d8be84d47974d4703310301&short=https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978&name=cs1948`
   3. call REST API: 
   4. 分析返回值
   
Example:
```
python3 ex1-cutt.ly.py https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978 cs1948

--- 命令行参数: ['ex1-cutt.ly.py', 'https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978', 'cs1948']
--- api_url:  https://cutt.ly/api/api.php?key=e77a2e10762f46d8be84d47974d4703310301&short=https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978&name=cs1948
--- data:  {'status': 7, 'fullLink': 'https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978', 'date': '2021-03-07', 'shortLink': 'https://cutt.ly/cs1948', 'title': 'Example Domain'}
--- Shortened URL: https://cutt.ly/cs1948
```

### Bit.ly 网站和API

1. 注册
2. 查阅API 文档: https://dev.bitly.com/api-reference#createBitlink
5. Python 六部分:
   1. 获取参数
   2. 第一个REST API Call 获取 Bearer Token (验证码) : https://api-ssl.bitly.com/oauth/access_token => e65420c4b8961ac44590cbb8644724245c0c82c9
   3. 第二个REST API Call 获取 group_guid : https://api-ssl.bitly.com/v4/groups
   4. 构建第三个REST API URL: ("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
   5. 第三个REST API call: 
   6. 分析返回值

Example:
```
python3 ex1-bit.ly.py  https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978

--- 命令行参数: ['ex1-bit.ly.py', 'https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978']
--- Got access token: e65420c4b8961ac44590cbb8644724245c0c82c9
--- groups_res: {'groups': [{'created': '2021-03-07T01:07:01+0000', 'modified': '2021-03-07T01:07:01+0000', 'bsds': [], 'guid': 'Bl371Mwg2Dq', 'organization_guid': 'Ol371eV3Vgq', 'name': 'cs1948', 'is_active': True, 'role': 'org-admin', 'references': {'organization': 'https://api-ssl.bitly.com/v4/organizations/Ol371eV3Vgq'}}]}
--- guid: Bl371Mwg2Dq
--- Shortened URL: https://bit.ly/38iYva9
```