import requests
import os
names=[]
url_lists=[]
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
}
def read_file():
    with open('names.txt', 'r') as f:
        for name in f:
            names.append(name.replace('\n', ''))
    with open('list_urls.txt', 'r') as f:
        for url in f:
            url_lists.append(url.replace('\n', ''))
def down_img():
    total_index = 0
    for name in names:
        file = '王者荣耀皮肤壁纸/' + name
        try:
            os.mkdir(file)
        except FileExistsError:
            i = 1
            while os.path.exists(file + str(i)):
                i += 1
            file = file + str(i)
            os.mkdir(file)
        except OSError:
            file = file.replace(':', '')
            os.mkdir(file)
        for index in range(7):
            re = requests.get(url_lists[index + 7 * total_index], headers=headers)
            with open(file + '/' + str(index) + '.jpg', 'wb') as f:
                f.write(re.content)
        total_index += 1
read_file()
down_img()



