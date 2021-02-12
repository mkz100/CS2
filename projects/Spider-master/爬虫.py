# 导入模块
from bs4 import BeautifulSoup     # 网页解析， 获取数据
import re       # 正则表达式， 进行文字匹配
import urllib.request, urllib.error     # 指定URL， 获取网页数据
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLite数据库操作



def main():
    baseurl = "https://movie.douban.com/top250?start="

    # 1. 爬取网页  2. 解析数据 
    datalist = getData(baseurl)     # 调用getData函数， 并将返回的内容放入datalist里面

    # 3.1 保存数据到Excel
    savepath = '豆瓣电影Top250.xls'
    saveData(datalist, savepath)              # 调用存储函数
   
    # # 3.2 保存数据到数据库
    dbpath = 'movie.db'
    saveData2DB(datalist, dbpath)
    


    # askURL("https://movie.douban.com/top250?start=0")

# =================================================正则表达式规则==================================================
# 正则表达式规则

# 影片详情链接的规则
findlink = re.compile(r'<a href="(.*?)">')     # re.compile 创建正则表达式对象， 表示规则（字符串的模式）

# 影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) # re.S表示： 忽略里面的换行符/，让换行符包含在字符中

# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')

# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')

# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')

# 找到影片的详情介绍
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)



# ===============================================1.0 爬取单个网页=================================================================
# 得到指定一个URL的网页的内容
def askURL(url):
    # 用户代理， 表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    # head = {     # 模拟浏览器头部信息， 向豆瓣服务器发送消息
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    # }        # 如果很多，就用列表的形式里面嵌套一个一个的

    head = {                #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
  

    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        pass
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html


# ========================================================1.1 加上for循环，爬取多个网页===============================================
# 1. 爬取网页函数
def getData(baseurl):
    datalist = []
    for i in range(0, 10):      # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)      # 保存获取到的网页源码： askURL函数返回的值保存到html  

        # ===============================================2.0 解析数据的================================================================

        # 2. 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')   # 将html按照html.parser方式进行解析，然后赋给对象soup
        for item in soup.find_all('div', class_='item'):    # 查找符合要求的字符串，形成列表  -- 本句意思：利用find_all()查找div里面class=items的内容
            # print(item)       # 测试： 查看电影item全部信息

            data = []           # 保存一部电影的所有信息
            item = str(item)    

            # 正则表达式的应用

            # (1). 获取影片详情的链接
            link = re.findall(findlink, item)[0]     # re库用来通过正则表达式查找指定的字符串   --  re.findall(查找规则， 被查找对象) [0]表示选择第一个元素
            data.append(link)                        # 添加链接

            # (2). 获取影片图片的链接
            imgSrc = re.findall(findImgSrc, item)[0] 
            data.append(imgSrc)                      # 添加图片

            # (3). 获取标题  -- 标题可能不止一个
            titles = re.findall(findTitle, item)      # 片名可能只有一个中文名，没有外文名 -- 存储的时候，要判断
            if (len(titles) == 2):
                ctitle = titles[0]                    # 中文名
                data.append(ctitle)
                ftitle = titles[1].replace('/', '')   # 外文名
                data.append(ftitle)
            else:
                data.append(titles[0])
                data.append('')                      # 外文留空

            # (4). 获取评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # (5). 获取评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            # (6). 获取影片概况 -- 概况可能为空
            inq = re.findall(findInq, item)
            if (len(inq) != 0):
                inq = inq[0].replace('。', '')      # 去掉句号
                data.append(inq)
            else:
                data.append('')
            
            # (7). 获取影片的详情介绍  -- 需要对详情进行处理
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', '', bd)    # 去掉<br/>
            bd = re.sub('/', '', bd)       # 替换/
            data.append(bd.strip())         # strip()去掉空格

            datalist.append(data)       # 把处理好的一部电影信息放入datalist

    return datalist


# ===============================================3.0 保存到Excel函数=================================================================
def saveData(datalist, savepath):
    print('正在保存.......')
    # 创建workbook对象
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 创建工作表
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)

    # 创建一个列的元组
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价数', '概况', '相关信息')

    for i in range(0, 8):
        # 写入数据， 第一行参数为‘行’， 第二行参数为‘列’， 第三行参数为内容
        sheet.write(0, i, col[i])   # 写入列的数据

    for i in range(0, 250):
        print(f'正在写入第{i+1}条')
        data = datalist[i]      # 因为datalist是列表的嵌套，所以要一个信息的传
        # 传第单个信息
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])    # 保存数据

    # 保存数据表
    book.save(savepath) 



# ===============================================3.1 保存到SQLite数据库=================================================================
def saveData2DB(datalist, dbpath):
    Init_db()
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:   # 250行
        for index in range(len(data)):  # 8列
            if index == 4 or index == 5:
                continue        # 如果是第五列和第六列是不需要加''的，是int型；直接退出本次小循环，继续下面的循环
            data[index] = '"' + data[index] + '"'   # 因为SQL语句是有''的
        
        sql = '''
            insert into movie250(
            info_link, pic_link, cname, fname, score, rated, instr, info)
            values(%s)'''%",".join(data)

        cur.execute(sql)
        conn.commit()
    
    cur.close()
    conn.close()



def Init_db(dbpath):
    sql = '''
        create table movie250
        (
        id interger primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        fname varchar,
        score numeric,
        rated numeric,
        instr text,
        info text
        );
    '''      # 创建数据表
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()








if __name__ == "__main__":
    main()
    print('*'*20)
    print('爬取完成！')