# 爬取王者荣耀皮肤
### 各代码功能
#### crape_pic_urls_and_names.py
用于爬取王者荣耀官网的的皮肤名字以及url,并且将皮肤名字存入names.txt，url存入list_urls.txt中

#### scrape_wangzheronyao.py
 用于爬取解析下来的name.txt和list_urls.txt,用于下载图片（没有使用多线程，所以时间消耗可能比较大）
 
### 解释
使用到python的库selenium和requests,由于王者荣耀官网使用Javascipt渲染，直接使用requests比较复杂，配合driver.Edge来模拟点击浏览器的行为(需要配置WebDriver，可以网上搜索来配置，参考网址：[配置环境](https://blog.csdn.net/xp178171640/article/details/115343585))，其中需要根据Xpath来寻找相应规律(Xpath真的很好用啊，直接右击复杂Xpath的路径就可以了)