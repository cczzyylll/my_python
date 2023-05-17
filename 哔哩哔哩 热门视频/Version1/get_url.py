#获取b站热门视频前500
from selenium import webdriver
url_Xpath='//*[@id="app"]/div/div[2]/div[1]/ul/div[{id}]/div[1]/a'
driver=webdriver.Edge()
def get_url():
    driver.get('https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0')
    js = "window.scrollTo(0,document.body.scrollHeight)"
    for i in range(0, 5000):
        driver.execute_script(js)
    for id in range(1, 501):
        with open('bilibili.txt','a') as f:
            f.write(driver.find_element_by_xpath(url_Xpath.format(id=id)).get_attribute('href')+'\n')
def main():
    get_url()
if __name__=='__main__':
    main()