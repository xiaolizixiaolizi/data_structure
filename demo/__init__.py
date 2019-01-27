from urllib import request
from base64 import b64encode
import requests

# 调用阿里云接口自己在后面加上?type=e或者?type=n或者?type=ne
regonize_url = 'http://route.showapi.com/184-5'
response = requests.get(regonize_url)
print(response.status_code)
# a_url='https://302307.market.alicloudapi.com/ocr/captcha/ocr/captcha'
#
# # 下载图片并且把图片给编码b64格式
# captcha_url = 'https://www.douban.com/misc/captcha?id=kbTehagzBECVVf5q8Yl5pbmD:en&size=s'
# request.urlretrieve(captcha_url, 'captcha.png')
#
# form_data ={}
# with open('captcha.png', 'rb')as fp:
#     data = fp.read()
#     pic = b64encode(data)
#     form_data['pic']=pic
#
# print(pic)
# # 定义头部信息
# appcode = 'b66a4c274b964ef88ca315743cf59a9e'
# headers = {
#     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#     'Authorization': 'APPCODE ' + appcode
# }
#
# # 发送post请求
# response=requests.post(a_url,data=form_data,headers=headers)
# print(response.json())
