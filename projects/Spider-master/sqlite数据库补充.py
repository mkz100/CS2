import sqlite3



# 1. 创建表

conn = sqlite3.connect('test.db')   # 打开或者创建数据库文件

print('成功打开数据库')

c = conn.cursor()     # 获取游标

"""
'单个是字符或字符串
''两个是段落
'''三个是段落

"""

sql = '''
    create table company     
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
    


c.execute(sql)      # 执行sql语句

conn.commit()       # 提交数据库操作

conn.close()        # 关闭数据库连接

print('成功建表')



# 2. 表插入数据
conn = sqlite3.connect('test.db')   # 打开或者创建数据库文件

print('成功打开数据库')

c = conn.cursor()     # 获取游标

"""
'单个是字符或字符串
''两个是段落
'''三个是段落

"""

sql = '''
    insert into company (id, name, age, address, salary)
     values (1, '张三', 32, '成都', 8000)
'''
    


c.execute(sql)      # 执行sql语句

conn.commit()       # 提交数据库操作

conn.close()        # 关闭数据库连接

print('成功插入数据')






# 3. 查询数据

conn = sqlite3.connect('test.db')   # 打开或者创建数据库文件
print('成功打开数据库')
c = conn.cursor()     # 获取游标

sql = 'select id, name, address, salary from company'
    
cursor = c.execute(sql)      # 执行sql语句, 查询有返回值

for row in cursor:
    print(f'id={row[0]}')
    print(f'name={row[1]}')
    print(f'address={row[2]}')
    print(f'salary={row[3]}')


conn.close()        # 关闭数据库连接

print('查询完毕')

