#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 17:08
# @Author  : eason.han
# @Email   : hanclong@hotmail.com
# @File    : load_mainpage.py
# @Software: PyCharm

import requests
import re
from urllib.parse import urlparse
def get_netloc():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    # driver = webdriver.Chrome(executable_path="./chromedriver-2")
    url = " https://cn.investing.com/indices/indices-cfds"
    # # driver.get(url,headers=headers)
    content = requests.get(url, headers=headers)
    content = content.content.decode(content.encoding)
    # content = open("./index.html","r",encoding="utf8").read()
    uri = re.search(r'https://stream[0-9|a-z|.]+.com',content).group()
    uri_info = urlparse(uri)
    return uri_info.netloc

if __name__ == '__main__':
    print(get_netloc())