import requests
import re
import  csv

poems = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}


def write_to_csv(data):
    with open('poem.csv','w',encoding='utf-8',newline='')as fp:
        header=['title','chaodai','author','content']
        writer=csv.DictWriter(fp,header)
        writer.writeheader()
        writer.writerows(data)


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)  # 所有的文章标题列表
    chaodais = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)  # 所有的朝代列表
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)  # 所有的朝代列表
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
    contents = []

    for content_tag in content_tags:
        x = re.sub(r'<.*?>', '', content_tag)  # 去杂质<br> 都是基于字符串string类型操作
        contents.append(x.strip())
    poems = []
    for title, chaodai, author, content in zip(titles, chaodais, authors, contents):
        poem = {
            'title': title,
            'chaodai': chaodai,
            'author': author,
            'content': content

        }
        poems.append(poem)

    write_to_csv(poems)







def spider():
    base_url = 'https://www.gushiwen.org/default_{}.aspx'
    for i in range(1, 2):
        url = base_url.format(i)
        parse_page(url)


if __name__ == '__main__':
    spider()
