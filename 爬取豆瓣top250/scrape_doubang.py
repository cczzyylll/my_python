import time

import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'Cookie':'douban-fav-remind=1; _vwo_uuid_v2=D0AA97F1A171AAB29F5FD1FB44D1EC1CE|be5299265179f4bae34407efa8fa823d; __utma=30149280.2142907953.1636774633.1651984660.1663383180.5; __utma=223695111.950000275.1648285397.1651985980.1663383180.4; __gpi=UID=00000535f6e8b234:T=1651985969:RT=1663383181:S=ALNI_MbZYMTev3eFkx8xTO10RjHQ5c7Frg; __yadk_uid=ypgEhkd7AUnnrLXRiDQVFHBPzEn0Pd8z; _pk_id.100001.4cf6=32b07e0f5a5d4434.1648285396.3.1663383787.1651986038.; bid=t0Ezs0Y_kP4; ll="118201"; ap_v=0,6.0; ct=y; dbcl2="254686698:jJvIgjRDi70"; ck=P4RI; frodotk_db="d50249ae61483f067f06dd0b23d8bd12"; push_noty_num=0; push_doumail_num=0'
}
page_url='https://movie.douban.com/top250?start={start}&filter='
detail_url='https://movie.douban.com/subject/1/'
urls=[]
def get_url(url):
    re=requests.get(url,headers=headers)
    re.encoding=re.apparent_encoding
    div_bf=BeautifulSoup(re.text,'lxml')
    divs=div_bf.find_all('div',{'class':'hd'})
    for div in divs:
        urls.append(div.find('a').get('href'))
def get_data(url):
    re=requests.get(url,headers=headers)
    re.encoding='utf-8'
    div_bf=BeautifulSoup(re.text.replace('<br />',''),'lxml')
    print(url)
    with open('豆瓣top250.txt','a',encoding='utf-8') as f:
        div_name=div_bf.find('div',{'id':'content'})
        f.write(div_name.find('h1').text.strip())
        f.write('\n')
        # print(div_name.find('h1').text.strip())
        div_actor=div_bf.find('div',{'class':'subject clearfix'})
        f.write(div_actor.text.strip())
        f.write('\n')
        # print(div_actor.text.strip())
        div_introduce=div_bf.find('div',{'class':'related-info'})
        f.write(div_introduce.find('h2').find('i').text.strip())
        f.write('\n')
        f.write(div_introduce.find('div',{'class':'indent'}).find('span').text.strip().replace(' ','').replace('\n',''))
        f.write('\n')
        # print(div_introduce.find('h2').find('i').text.strip())
        # print(div_introduce.find('div',{'class':'indent'}).find('span').text.strip().replace(' ','').replace('\n',''))
get_url(page_url)
for page in range(0,10):
    start=page*25
    get_url(page_url.format(start=start))
for url in urls:
    # time.sleep(1)
    get_data(url)
