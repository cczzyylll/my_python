# 爬取b站热门视频
### 主要代码解析
#### get_url.py:
用于爬取b站热门视频的URL,并且将URL存入bilibili.txt中
#### analy_urls:
用于解析爬取到的url，并且将视频的信息存入bilibili.csv中
### 使用的一些库
selenium
requests
csv
BeautifulSoup
### 作者:
cczzyy
### 更新时间
2023.5.17
### 改进方向
使用了正则表达式，来查找内容，比起BeautifulSoup库来说，在这里会更加方便一点，其他没什么