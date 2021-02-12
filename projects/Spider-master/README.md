# 说明：
这是学习bilibili李巍老师的豆瓣爬虫写得代码，所有代码全部出自李巍老师原创。本人只是用来学习练习，如有倾权行为，将在第一时间删除。
这是李巍老师的课程地址：
[课程地址](https://www.bilibili.com/video/BV12E411A7ZQ?p=27)


# Python爬虫和数据可视化

## 学习内容：
1. Python语言的基础知识
2. 网络爬虫的技术实现
3. 数据可视化的技术应用（框架、组件等）

## Python爬虫
* 任务介绍

  爬取豆瓣电影Top250的基本信息，包括电影的名称、豆瓣评分、评价数、电影概况、电影链接等。

[链接地址](https://movie.douban.com/top250)

![搜索引擎原理图](https://github.com/ShengtaoXu321/Picture/blob/master/搜索引擎原理.png)


## 爬虫的基本流程


* 准备工作

  通过浏览器查看分析目标网页， 学习编程基础规范。

* 获取数据

  通过HTTP库向目标站点发起请求，请求可以包含额外的header等信息，如果服务器能正常响应，会得到一个Response，便是所要获取的页面内容。

* 解析内容
  得到的内容可能是HTML、json等格式，可以用 `页面解析库` 、`正则表达式` 等进行解析。

* 保存数据
  保存形式多样，可以保存为文本，也可以保存到数据库，或者保存特定格式的文件。

### 准备工作

* 一、分析页面

* 二、编码规范
  
  1. 一般Python程序第一行需要加入 `# -*-doding:utf-8 -*-` 或者 `# coding=utf-8`这样可以在代码中包含中文
  
  2. 在Python中，使用函数实现单一功能或者相关功能的代码段，可以提高代码的可读性和重复利用率。

  3. Python文件中可以加入main函数用于测试程序 `if__name__ == "__main__":`

  4. Python使用 # 添加注释

* 三、引入模块
  模块（module）:用来逻辑上组织Python代码（变量、函数、类），本质就是py文件，提高diamagnetic的可维护性。

  ```Python
  import sys
  from bs4 import BeautifulSoup
  import urllib
  import xlwt
  ```

* 四、获取数据
  
  Python一般使用urllib2库获取页面

  获取页面数据
  
  1. 对于每一个页面， 调用askURL函数获取页面内容
  
  2. 定义一个获取页面的函数askURL,传入一个url参数，表示网址，如 https://movie.douban.com/top250?start=0

  3. urllib.request.Request生成请求；urllib.request.urlopen发送请求-获取响应；read获取页面内容

  4. 在访问页面时经常会出现错误，为了程序的正常运行，加入异常捕获try...except...


  ```Python
  # 得到页面全部内容  -- askURL函数
  def askURL(url):
    req = urllib.request.Request(url)  # 发送请求

    try:
      response = urllib.request.urlopen(req)  # 获取响应
      html = response.read()  # 获取网页内容传递给html变量
      print(html)

    except urllib.error.URLError as e:
      if hasattr(e, 'code'):
        print(e.code)'
      if hasatter(e, 'reason'):
        print(e.reason)

    return html
  ```

* 五、解析内容

  对爬取的html文件进行解析

  ```Python
  soup = BeautifulSoup(html, 'html.parser')
  for item in soup.find_all('div', class_='item'):  # 找到每一个影片项
    data = []
    item = str(item)  # 转换成字符串
    # 影片详情链接
    link = re.findall(findLink, item)[0]
    data.append(link)   # 添加详情链接

    imgSrc = re.findall(findImgSrc, item)[0]
    data.append(imgSrc)   # 添加图片链接

    titles = re.findall(findTitle, item)
    # 片名可能只有一个中文名，没有外国名
    if len(titles) == 2:
      citile = titles[0]
      data.append(ctitle)   # 添加中文片名
      otitle = titles[1].replace('/', '')
  ```


* 六、 保存数据
  
  Excel表存储
  利用Python库xlwt将抽取的数据datalist写入Excel表格
  ```Python
  # 程序调用面
  savepath = u'/home/aistudio/data/豆瓣电影Top250.xls'
  saveData(datalist, savepath)

  def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ('电影详情链接', '图片链接', '影片的中文名', '影片的外文名', '评分', '评价数', '概况', '相关信息')

  # 写入数据
    for i in range(0, 8):
      sheet.write(0, i, col[i])   # 列名

    for i in range(0, 250):
      data = datalist[i]
      for j in range(0, 8): 
        sheet.write(i+1, j, data[i])  # 数据
    
    book.save(savepath)   # 保存文件
  ```

  







