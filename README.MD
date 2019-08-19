# IP 代理池

## 开启代理池
直接执行`run.py`文件
```python
python run.py
```
服务启动后，等待代理池运行几分钟，采集并检测IP稳定后再使用。<br>
获取代理 IP 有三个接口，分别是：
- `http://localhost:5000/random`    随机获取一个可用代理
- `http://localhost:5000/all`   获取所有可用代理
- `http://localhost:5000/count` 获取可用代理的总数

## 使用方法
以python的requests为例
```python
import requests

def get_proxy():
    proxy = requests.get('http://localhost:5000/random').text
    return proxy
    
def test():
    r = requests.get('http:www.baidu.com',timeout=10,proxies={'http':'http://'+get_proxy()})

```

## 软件环境
- python 3.6x
- redis

## 第三方库
- Flask==0.12
- requests==2.20.0
- redis==3.0.1
- aiohttp==3.5.4
- lxml==3.7.2
- beautifulsoup4==4.8.0

## 新增代理
在`crawler.py`文件下的`Crawler`类中，新增名称以`crawl_`开头的方法来采集对应网站的IP即可。