# 什么是BeautifulSoup4?
# '''
# BS4： 将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所欲对象可以归纳为4种：

# - Tag
# - NavigableString
# - BeautifulSoup
# - Comment
# '''

from bs4 import BeautifulSoup

f = open('./baidu.html', 'rb')    # 以rb模式打开文件
html = f.read()             # 读取文件到html变量
bs = BeautifulSoup(html, 'html.parser')     # 使用BS解析html文件，使用html.parser解析器；解析完赋值到bs对象




print(bs.title)         # <title>百度一下，你就知道 </title>
print(bs.a)
print(bs.head)


# 1. Tag    标签及其内容： 拿到它所找到的第一个内容
print(type(bs.head))    # <class 'bs4.element.Tag'>

print(bs.title.string)  # 百度一下，你就知道


# 2. NavigableString    标签里面的内容(字符串)
print(type(bs.title.string))    # <class 'bs4.element.NavigableString'>

# 拿到一个标签里面所有的属性
print(bs.a.attrs)   # {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}


# 3. BeautifulSoup      表示整个文档
print(type(bs))         # <class 'bs4.BeautifulSoup'>
print(bs.name)
print(bs.attrs)


# 4. Comment        是一个特殊的NavigableString, 输出内容不包含注释符号
print(type(bs.a.string))    # 新闻


# =============================================================================================================

# 应用

# 1. 文档的遍历
print(bs.head.contents)     # 以列表的形式 返回一个head里面的数据
print(bs.head.contents[1])  # <meta content="text/html;charset=utf-8" http-equiv="content-type"/>


# 2. 文档的搜索

# (1). fina_all() 用法： 查找所有

# 字符串过滤： 会查找与字符串完全匹配的内容
t_list = bs.find_all('a')   # 查找所有的a标签的内容, 放进列表
print(t_list)

# 使用 正则表达式搜索： 使用search()方法来匹配内容
import re
t_list = bs.find_all(re.compile('a'))  # 使用正则表达式还是用 标签来匹配

# 方法 ： 传入一个函数（方法），根据函数的要求来搜索
def  name_is_exists(tag):
    return tag.has_attrs('name')

t_list = bs.find_all(name_is_exists)
# 列表的形式打印
for i in t_list:
    print(i) 


# (2). kwargs    参数搜索
# t_list = bs.find_all(id = 'head')
# t_list = bs.find_all(class_ = True)
# t_list = bs.find_all(herf = 'http://news.baidu.com')


# for i in t_list:
#     print(i)


# (3). text 参数
# t_list = bs.find_all(text = 'hao123')
t_list = bs.find_all(text = ['hao123', '贴吧', '地图'])

t_list = bs.findP_all(text = re.compile('\d'))  # 应用 正则表达式 来查找包含特定文本的内容（标签里的字符串）

for i in t_list:
    print(i)


# (4). limit参数
t_list = bs.find_all('a', limit = 3)    # limit限定参数
print(t_list)




# ================================================================================================================
# CSS选择器

list1 = bs.select('title')    # 通过标签来查找

list1 = bs.select('.mnav')    # .表示类，后面是类名 -- 通过类名来查找

list1 = bs.select('#u1')      # 通过id来查找

list1 = bs.select("a[class = 'bri']")   # 通过属性来查找

list1 =  bs.select('head > title')      # 通过head下面的title子标签进行来查找
 
list2 = bs.select('.mnav ~ .bri')       # 通过兄弟节点类查找 -- 就是.mnav里面的bri属性
print(list2[0].get_text())              # .get_text()是为了得到列表里面的内容，列表下标切片访问
print(list1)
for i in list1:
    print(i)