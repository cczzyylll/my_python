import csv
import requests
from bs4 import BeautifulSoup
def analy_url(url):
    re = requests.get(url)
    re.encoding = 'utf-8'
    bf = BeautifulSoup(re.text, 'lxml')
    try:
        title=bf.find('h1', {'class': 'video-title tit'}).text
        views=bf.find('span', {'class': 'view item'}).get('title').replace('总播放数','')
        barrage=bf.find('span', {'class': 'dm item'}).get('title').replace('历史累计弹幕数','')
        time=bf.find('span', {'class': 'pudate'}).get('title')
        list_4=bf.find_all('span', {'class': 'info-text'})
        like=list_4[0].text
        coin = list_4[1].text
        collect = list_4[2].text
        forward= list_4[3].text
    except AttributeError:
        title=views=barrage=time=like=coin=collect=forward='null'
    try:
        author=bf.find('a', {'class': 'username'}).text.strip()
    except AttributeError:
        try:
            author=bf.find('a',{'class':'upname is-vip'}).text.strip()
        except AttributeError:
            author='null'
    try:
        attention_num=bf.find('span', {'class': 'has-charge'}).text.strip().replace('关注','')
    except AttributeError:
        try:
            attention_num=bf.find('div',{'class':'default-btn follow-btn btn-transition b-gz not-follow'}).text.strip().replace('关注','')
        except AttributeError:
            attention_num='多名up主参与'
    # print(url)
    # print(title,views,barrage,time,like,coin,collect,forward,author,attention_num)
    write_to_csv(title,views,barrage,time,like,coin,collect,forward,author,attention_num)
def init_csv():
    headers=['标题','总播放量','积累弹幕','时间','点赞','投币','收藏','转发','作者','关注量']
    with open('bilibili.csv','a',encoding='utf-8-sig',newline='') as f:
        write=csv.writer(f)
        write.writerow(headers)
def write_to_csv(title,views,barrage,time,like,coin,collect,forward,author,attention_num):
    list=[title,views,barrage,time,like,coin,collect,forward,author,attention_num]
    with open('bilibili.csv','a',encoding='utf-8-sig',newline='') as f:
        write=csv.writer(f)
        write.writerow(list)
def get_urls():
    urls_list=[]
    with open('bilibili.txt','r') as f:
        for line in f:
            urls_list.append(line.replace('\n',''))
    for url in urls_list:
        analy_url(url)
def main():
    init_csv()
    get_urls()
if __name__=='__main__':
    main()