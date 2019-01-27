import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

def parse_page(url):
    response=requests.get(url,headers=headers)
    text=response.text

    username_tags=re.findall(r'<div class="author clearfix">.*?<h2>(.*?)</h2>',text,re.DOTALL)
    usernames=[]
    for username_tag in username_tags:
        x=re.sub(r'\s?','',username_tag)
        usernames.append(x)

    content_tags=re.findall(r'<div class="content">.*?<span>(.*?)</span>',text,re.S)
    contents=[]
    for content_tag in content_tags:
        x=re.sub(r'<.*?>','',content_tag)
        contents.append(x.strip())

    lists=[]

    for username,content in zip(usernames,contents):
        list={
            'username':username,
            'content':content
        }
        lists.append(list)


    for list in lists:
        print(list)










def spider():
    base_url='https://www.qiushibaike.com/text/page/{}/'
    for i in range(1,2):
        url=base_url.format(str(i))
        parse_page(url)



if __name__ == '__main__':
    spider()