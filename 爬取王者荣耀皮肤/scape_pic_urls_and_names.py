from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests

browser = webdriver.Edge()
xpath_img = '//*[@id="Work_List_Container_267733"]/div[{num}]/img'
page_javascript = '//*[@id="Page_Container_267733"]/a[{id}]'
# 打开图片后8张图片
img_li = '//*[@id="paper_desc"]/ul/li[{num}]/a'
# 一页的20块图片
img_div = '//*[@id="Work_List_Container_267733"]/div[{id}]/h4/a'
browser.get('https://pvp.qq.com/web201605/wallpaper.shtml')


# 爬取一整页图片
def scrape_one_page():
    img_url = []
    names = []
    for div_click in range(1, 21):
        browser.find_element_by_xpath(img_div.format(id=div_click)).click()
        names.append(browser.find_element_by_xpath('//*[@id="paper_curname"]').text)
        for li_click in range(1, 8):
            img_url.append(browser.find_element_by_xpath(img_li.format(num=li_click)).get_attribute('href'))
        browser.find_element_by_xpath('//*[@id="paper_downalertBoxs"]/a').click()
    return img_url, names


def scrape_one_page33():
    img_url = []
    names = []
    for div_click in range(1, 7):
        browser.find_element_by_xpath(img_div.format(id=div_click)).click()
        names.append(browser.find_element_by_xpath('//*[@id="paper_curname"]').text)
        for li_click in range(1, 8):
            img_url.append(browser.find_element_by_xpath(img_li.format(num=li_click)).get_attribute('href'))
        browser.find_element_by_xpath('//*[@id="paper_downalertBoxs"]/a').click()
    return img_url, names


def switch_page(page):
    element = browser.find_element_by_xpath(page_javascript.format(id=page))
    element.click()


# def down_img(list_urls, names):
#     i = 0
#     for name in names:
#         file = '王者荣耀皮肤壁纸/' + name
#         os.mkdir(file)
#         for j in range(8):
#             re=requests.get(list_urls[j+i*8])
#             with open(str(j) + '.jpg', 'wb') as f:
#                 f.write(re.content)
#         i += 1
def down_tetx(list_urls,names):
    with open('list_urls.txt','a') as f:
        for url in list_urls:
            f.write(url+'\n')
    with open('names.txt','a') as f:
        for name in names:
            f.write(name+'\n')

for page in range(2, 12):
    switch_page(page)
    down_tetx(*scrape_one_page())
browser.find_element_by_xpath('//*[@id="Page_Container_267733"]/a[13]').click()
for page in range(3, 13):  # 3-12
    switch_page(page)
    down_tetx(*scrape_one_page())
browser.find_element_by_xpath('//*[@id="Page_Container_267733"]/a[14]').click()
for page in range(3, 13):  # 3-12
    switch_page(page)
    down_tetx(*scrape_one_page())
browser.find_element_by_xpath('//*[@id="Page_Container_267733"]/a[14]').click()
down_tetx(*scrape_one_page())
switch_page(4)
down_tetx(*scrape_one_page())
switch_page(5)
down_tetx(*scrape_one_page33())