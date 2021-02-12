import xlwt


# 1. 创建workbook对象
workbook = xlwt.Workbook(encoding='utf-8')

# 2. 创建工作表
worksheet = workbook.add_sheet('sheet1')

# 3. 写入数据， 第一行参数为‘行’， 第二行参数为‘列’， 第三行参数为内容
worksheet.write(0, 0, 'hello')

# 保存数据表
workbook.save('student.xls') 



# 应用一： 九九乘法表
# for循环实现
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('九九乘法表')

for i in range(1, 10):
    for j in range(1, i+1):
        worksheet.write(i-1, j-1, f'{i} * {j} = {(i)*(j)}')

workbook.save('student.xls')


# while循环实现
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('九九乘法表')

i = 1
while i < 10:
    j = 1
    while j <= i:
       worksheet.write(i-1, j-1, f'{i} * {j} = {(i)*(j)}')
       j += 1
    i +=1
 
workbook.save('student.xls')