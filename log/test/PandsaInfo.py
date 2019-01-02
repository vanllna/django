import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



'''  
pdinfo = pd.read_excel(r'D:\pro\log\test\book.xlsx',skiprows=3,usecols='C:F',dtype={'id':str,'instore':str,'date':str})
for i in pdinfo.index:
    pdinfo['id'].at[i]= i+1
    pdinfo['instore'].at[i] = 'yes' if i % 2 == 0 else 'no'
    pdinfo['date'].at[i] = datetime.now()

pdinfo.set_index('id',inplace=True)
print(pdinfo)
 '''


'''   
s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([10,20,30],index=[1,2,4],name='C')
df = pd.DataFrame({s1.name:s1 , s2.name:s2 , s3.name:s3}) #以字典的形式加入数据 为以 列 的形式返回
print(df)
print('===============')
du = pd.DataFrame([s1,s2,s3]) #以列表的形式加入数据 为以 行 的形式返回
print(du)
'''

'''  
readinfo = pd.read_excel(r'D:\pro\log\test\output.xlsx')
readinfo['price'] = readinfo['listprice'] + readinfo['discount']
readinfo['price'] = readinfo['price'].apply([lambda x:x+2])
readinfo.sort_values(by=['listprice'],inplace=True,ascending=[True])
# readinfo = readinfo.loc[readinfo['listprice'].apply(lambda x:100<x<500)]
# readinfo.plot.bar(x='name',y=['listprice','price'])  #bar 竖形图
#readinfo.plot.barh(x='name',y=['listprice','price'],stacked=True)  #barh 横向图   stacked 把Y轴上多组的数据合在一条轴上
# readinfo['listprice'].plot.pie(counterclock=False,startangle=-220) # pie 饼图
#readinfo.plot.area(x='name',y=['listprice','price'])  # 折线图
# readinfo.plot.scatter(x='listprice',y='price')  #散点图
readinfo['price'].plot.hist(bins=500)  # 直方图
ax = plt.gca()
ax.set_xticklabels(readinfo.name)
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('interlation field')
plt.tight_layout()
plt.show()
print(readinfo)

'''

'''  自动填充空白格内容
students = pd.read_excel(r'D:\pro\log\test\Student_Score.xlsx',index_col='ID')
scores = pd.read_excel(r'D:\pro\log\test\Student_Score.xlsx',sheet_name='Scores',index_col='ID')
tables = students.join(scores,how='left').fillna(0)
# print(students)
# scorefilter = tables.loc[tables['Score'].apply(lambda x:80<x<90)]

def students_vaidation(row):
    if 60 < row.Score <85:
        print('student is %s , has invalid score %s'%(row.Name,row.Score))
tables = tables.loc[tables['Score'].apply(lambda x:60<x<85)]

# print(tables)
print(tables)

'''

'''   一列数据 分成多列
readinfo = pd.read_excel(r'D:\pro\log\test\Employees.xlsx')
df = readinfo['Full Name'].str.split(expand=True)

readinfo['first name'] = df[0]
readinfo['last name'] = df[1]
print(readinfo)

'''

'''  分行统计
pd.options.display.max_columns = 777
students = pd.read_excel(r'D:\pro\log\test\Students.xlsx',index_col='ID')
temp = students[['Test_1','Test_2','Test_2']]
row_sum = temp.sum(axis=1)
row_avg = temp.mean(axis=1)
students['row_sum'] = row_sum
students['row_avg'] = row_avg.astype(int)
col_mean = students[['Test_1','Test_2','Test_3','row_sum','row_avg']].mean()
col_mean['Name'] = 'Summary'

students = students.append(col_mean,ignore_index=True)
print(students)
'''

'''   去重
readinfo = pd.read_excel(r'D:\pro\log\test\Students_Duplicates.xlsx')
# readinfo.drop_duplicates(subset='Name',inplace=True,keep='first')
dupe = readinfo.duplicated(subset='Name')
dupe = dupe[dupe]
print(readinfo.loc[dupe.index])
'''
'''  
pd.options.display.max_columns = 777
readinfo = pd.read_excel(r'D:\pro\log\test\Videos.xlsx',index_col='Month')
table = readinfo.transpose()
'''


'''   透视表
pd.options.display.max_columns = 777
readinfo = pd.read_excel(r'D:\pro\log\test\Orders.xlsx')
readinfo['Year'] = pd.DatetimeIndex(readinfo['Date']).year
pv1 = readinfo.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)

groups = readinfo.groupby(['Category','Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pv2 = pd.DataFrame({'Total':s,'Count':c})

print(pv2.head(15))
 '''


readinfo = pd.read_excel(r'D:\pro\log\test\Students.xlsx')
stu = pd.Series({'ID':21,'Name':'uouo','Test_1':99,'Test_2':98,'Test_3':97})
readinfo = readinfo.append(stu,ignore_index=True).reset_index(drop=True)
readinfo.drop(index=readinfo.index[20],inplace=True)
print(readinfo)







