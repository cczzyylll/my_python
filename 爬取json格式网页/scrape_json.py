import requests
import logging
import os
requests.packages.urllib3.disable_warnings()
logging.basicConfig(level=logging.ERROR,format='%(asctime)s:%(message)s')
Page_url='https://spa1.scrape.center/api/movie/?limit=10&offset={offset}'
Detail_url='https://spa1.scrape.center/api/movie/{id}/'
def scrape_url(url):
    logging.info('scraping %s',url)
    try:
        re=requests.get(url,verify=False)
        if re.status_code==200:
            return re.json()
        logging.info('Fail to scrape %s because of the status code is %s',url,re.status_code)
    except requests.RequestException:
        logging.info('Fail to scrape %s because of error',url)
def scrape_page(page):
    page=page*10
    url=Page_url.format(offset=page)
    return scrape_url(url)
def scrape_id(id):
    url=Detail_url.format(id=id)
    return scrape_url(url)
def main():
    for page in range(0,10):
        page_data=scrape_page(page)
        for item in page_data.get('results'):
            id_text=scrape_id(item.get('id'))
            with open('电影.txt','a',encoding='utf-8') as f:
                f.write(id_text.get('name')+'-'+id_text.get('alias'))
                f.write('\n')
                f.write(' '.join(id_text.get('categories')))
                f.write('\n')
                f.write('、'.join(id_text.get('regions'))+'/'+str(id_text.get('minute'))+'分钟')
                f.write('\n')
                f.write(str(id_text.get('published_at'))+"上映")
                f.write('\n')
                f.write('剧情简介：')
                f.write('\n')
                f.write(id_text.get('drama'))
                f.write('\n')
                f.write('\n')
            # print(id_text.get('name')+'-'+id_text.get('alias'))
            # print(' '.join(id_text.get('categories')))
            # print('、'.join(id_text.get('regions'))+'/'+str(id_text.get('minute'))+'分钟')
            # print(str(id_text.get('published_at'))+"上映")
            # print('剧情简介：')
            # print(id_text.get('drama'))
if __name__=='__main__':
    main()