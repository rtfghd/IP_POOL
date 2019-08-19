# IP代理池-获取模块

import json,redis,time
from random import choice
import requests,lxml
from bs4 import BeautifulSoup

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('获取代理成功',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_kuaidaili(self,page_count=10):
        '''
        获取 快代理
        :param page_count: 页码
        :return: 代理
        '''
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = requests.get(url)
            time.sleep(1)
            soup = BeautifulSoup(html.text, 'lxml')
            trs = soup.select('#list > table > tbody > tr')
            for tr in trs:
                ip = tr.select('td:nth-of-type(1)')[0].text
                port = tr.select('td:nth-of-type(2)')[0].text
                yield ':'.join([ip, port])

