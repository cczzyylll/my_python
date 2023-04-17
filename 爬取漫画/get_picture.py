import encodings
import os
import requests
from bs4 import BeautifulSoup
import time
import  threading
class download(object):
    def __init__(self):
        self.urls=[]
        self.names=[]
        self.target="http://guashuoshuo.com/comic/huangfeijialin.html"
    def get_urls(self):
        re=requests.get(self.target)
        re.encoding=re.apparent_encoding
        html=re.text
        li_bf=BeautifulSoup(html,'lxml')
        li=li_bf.find_all("li",class_='item')
        a_bf=BeautifulSoup(str(li),'lxml')
        a=a_bf.find_all('a')
        for i in a[3:]:
            self.urls.append("http://guashuoshuo.com"+i.get('href'))
            self.names.append(i.get('title'))
    def get_one_url(self,i):
        re = requests.get(i)
        html = re.text
        img_bf = BeautifulSoup(html, 'lxml')
        img = img_bf.find_all('img', class_="lazy-read")
        for x in img:
            img_url = x.get("data-original")
            re = requests.get(img_url)
            folder_name = self.names[self.urls.index(i)]
            folder_name = folder_name.rstrip()
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            file_name = x.get('alt')
            file_path = os.path.join(folder_name, file_name)
            print(file_path)
            img_data = re.content
            # file_path=file_path.encode("utf-8")#编码为utf-8
            # file_path=os.path.abspath(file_path)#获取绝对路径
            with open(file_path, 'wb') as f:
                # # # with open(x.get('alt'),'wb') as f:
                f.write(img_data)
    def get_img(self):
        threads=[]
        for i in self.urls:
            time.sleep(5)#暂停5秒
            thread=threading.Thread(target=self.get_one_url,args=(i,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
if __name__=="__main__":
    x=download()
    x.get_urls()
    x.get_img()

    # print(x.names)
    # download_header = {
    #     'Referer': 'http://guashuoshuo.com/chapter/55509_740043.html'
    # }
    # re1=requests.get('http://guashuoshuo.com/chapter/55509_740043.html')
    # cookies=re1.cookies
    # headers = {
    #     'Referer':"http://guashuoshuo.com/chapter/55509_740043.html"
    # }
    # ur="https://tu10.zifanshumh.com/attachment/comic/gd/g6gg/DB9F7D36A77C886CC47A90DD077B7EEF.jpg"
    # image_data=re.content
    # with open("2.jpg",'wb') as f:
    #     f.write(image_data)