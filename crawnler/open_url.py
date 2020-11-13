
# encoding:utf-8

import time

import requests



def cookie_str2equ(str):
    file = open("cookie.txt", "w")
    list = str.split(";")
    for x, item in enumerate(list):
        list[x] = item.strip()
    for item in list:
        key, value = item.split("=")
        file.write(key + " = \"" + value + "\",\n")


def open_url(url):

    # url_decode = urllib.parse.quote(url)

    print("open", url, sep=":")
    # 正常的方式进行访问
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    # }
    # 携带cookie进行访问
    cookie = open("cookie.txt").read()
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Cookie': cookie,
    }

    conn = requests.session()
    response = conn.get(url, headers=headers)

    # time.sleep(0.1)
    str = response.text


    # 输出所有
    # print(response.read().decode('gbk'))
    # 将内容写入文件中
    with open('test.html', 'w', encoding="utf-8") as fp:
        fp.write(str)
    return str.replace("<br>", "<br/>")

if __name__ == '__main__':
    # open_url("https://www.qichacha.com/firm_9f4adeb723cc71f8f60a989f885482e1.html")
    open_url("https://www.qichacha.com/search?key=%E5%BC%A0%E5%8B%87")