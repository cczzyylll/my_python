import csv
import requests
import re as regex
from bs4 import BeautifulSoup
def analy_url(url):
    re = requests.get(url)
    re.encoding = 'utf-8'
    bf = BeautifulSoup(re.text, 'lxml')
    try:
        title=bf.find('h1', {'class': 'video-title tit'}).text
        views=regex.search('视频播放量\s+\d+',re.text).group().replace('视频播放量 ','')
        barrage=regex.search('弹幕量\s+\d+',re.text).group().replace('弹幕量 ','')
        time=bf.find('span', {'class': 'pudate'}).get('title')
        like=regex.search('点赞数\s+\d+',re.text).group().replace('点赞数 ','')
        coin = regex.search('投硬币枚数\s+\d+',re.text).group().replace('投硬币枚数 ','')
        collect = regex.search('收藏人数\s+\d+',re.text).group().replace('收藏人数 ','')
        forward= regex.search('转发人数\s+\d+',re.text).group().replace('转发人数 ','')

    except AttributeError:
        title=views=barrage=time=like=coin=collect=forward='null'
    try:
        author=regex.search('视频作者\s+.*?,',re.text).group().replace('视频作者 ','')[:-1]
    except AttributeError:
        author='null'
    try:
        authorIntro=regex.search('作者简介\s+.*?，',re.text).group().replace('作者简介 ','')[:-1]
    except AttributeError:
            authorIntro='多名up主参与'
    # print(url)
    # print(title,views,barrage,time,like,coin,collect,forward,author,attention_num)
    write_to_csv(title,views,barrage,time,like,coin,collect,forward,author,authorIntro)
def init_csv():
    headers=['标题','总播放量','积累弹幕','时间','点赞','投币','收藏','转发','作者','简介']
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
# import re
# import requests
# from bs4 import BeautifulSoup
# ree = requests.get('https://www.bilibili.com/video/BV1da4y1g7Df')
# ree.encoding = 'utf-8'
# bf = BeautifulSoup(ree.text, 'lxml')
# # title=bf.find('h1', {'class': 'video-title tit'}).text
# # print(title)
# # views=bf.find('span', {'class': 'view item'}).get('title').replace('总播放数','')
# # print(views)
# # barrage=bf.find('span', {'class': 'dm item'}).get('title').replace('历史累计弹幕数','')
# # time=bf.find('span', {'class': 'pudate'}).get('title')
# # list_4=bf.find('span', {'class': 'video-like-info video-toolbar-item-text'})
# # print(list_4.text)
# # time=bf.find('span', {'class': 'pudate'}).get('title')
# # print(time)
# # collect = bf.find('span', {'class': 'video-fav-info video-toolbar-item-text'}).text
# # print(collect)
# forward= bf.find('svg', {'class': 'video-share-icon video-toolbar-item-icon'})
# print(re.search('转发人数\s+\d+',ree.text).group().replace('转发人数 ',''))
# print(forward)
# # print(re.text)
# # # like=list_4[0].text
# # # coin = list_4[1].text
#
# # # collect = list_4[2].text
# # # forward= list_4[3].text