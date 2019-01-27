import re

# 匹配某个字符串
# text='hello'
# ret=re.match('he',text)
# print(ret.group())

# text='hello'
# ret=re.match('.',text)
# print(ret.group())
#
# text='0713-88-88888ppERR84545'
# ret=re.match('[\d\-]*',text)
# print(ret.group())
#
# text='hel232lo'
# ret=re.match('\w{5,7}',text)
# print(ret.group())
# 手机号码
# phone='18616010531'
# ret=re.match('1[34578]\d{9}',phone)
# print(ret.group())

# # 邮箱
# email='1756329434wqerW_R@163.com'
# ret=re.match('\w+@[0-9a-z]+\.[a-z]+',email)
# print(ret.group())
#
# # url
# url='https://www.hao123.com/?tn=97974706_hao_pg'
# ret=re.match('(http|https|ftp)://[^\s]+',url)
# ret1=re.match('[^\s]+',url)
# print(ret.group())

# 身份证
# text='421127199410180434'
# print(len(text))
# ret=re.match('\d{17}[\dxX]',text)
# print(ret.group())

# $结尾
# email='1756329434wqerW_R@163.com'
# ret=re.match('\w+@163.com$',email)
# print(ret.group())

# 匹配0-1000
# text='1000'
# ret=re.match('[1-9]\d{0,2}?$|1000$',text)
# print(ret.group())

# text = 'it is $266'
# ret = re.search('\$\d+', text)
# print(ret.group())

html = '''
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>岗位职责：</p>
<p>1、 数据的整理清洗，归档存储。&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>
<p>2、 业务统计需求&nbsp;</p>
<p>3、 统计技术框架的搭建和维护&nbsp;</p>
<p>任职要求：</p>
<p>&nbsp; 1、熟练掌握 python C C++ java等编程语言一种以上,熟练使用Linux操作系统，shell命令等 ；</p>
<p>&nbsp; 2、熟悉 mysql,redis,levelDB，Hadoop等；</p>
<p>&nbsp; 3、有处理海量日志经验。 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>
        </div>
    </dd>
'''
ret=re.sub('<.+?>','',html,)
print(ret)
