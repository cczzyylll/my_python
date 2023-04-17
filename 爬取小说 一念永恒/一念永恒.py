import requests
from bs4 import BeautifulSoup
class down:
    def __init__(self):
        self.urls=[]
        self.names=[]
        self.text=[]
    def get_urls(self):
        target='https://www.ddyueshu.com/1_1100/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        }
        re=requests.get(target,headers=headers)
        re.encoding=re.apparent_encoding
        html=re.text
        soup=BeautifulSoup(html,'lxml')
        all_a=soup.find_all('a')
        # for a in all_a[30:2071]:#爬取全部章节
        for a in all_a[30:33]:#爬取部分
            self.urls.append('https://www.ddyueshu.com'+a.get('href'))
            self.names.append(a.text)
    def get_text(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        }
        for url in self.urls:
            print('进度：%'+str(float(self.urls.index(url)/len(self.urls))))
            re=requests.get(url,headers=headers)
            re.encoding=re.apparent_encoding
            html=re.text
            soup=BeautifulSoup(html,'lxml')
            all_div = soup.find('div', id='content')
            self.text.append(all_div.text[:len(all_div.text) - 49])
    def write_to_file(self,file_path):
        for i in range(len(self.urls)):
            with open(file_path,'a') as f:
                f.write('                                                                                      '+self.names[i]+'\n'+self.text[i]+'\n'+'-------------------------------------------------------------------------------------------------------------------------------'*2+'\n')
if __name__=='__main__':
    a=down()
    a.get_urls()
    a.get_text()
    a.write_to_file('一念永恒.txt')



