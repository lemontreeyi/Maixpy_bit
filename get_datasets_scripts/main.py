import requests
import json
from urllib import request
import time

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}

url_list = []
dir_root = "./pic"
start_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8196848040350823503&ipn=rj&ct=201326592&is=&fp=result&fr=&word=字母A&queryWord=字母A&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1648694065606="


def download_pic(pic_url, num):
    file_name = f"{dir_root}/{num}.png"
    request.urlretrieve(pic_url, file_name)


def get_url(page_url):
    res = requests.get(page_url, headers=headers)
    dir = json.loads(res.text)
    # 获取存放图片url的字典
    pic_list = dir['data']
    for i in range(len(pic_list)-1):
        dict_page = pic_list[i]
        url_list.append(dict_page['thumbURL'])

def main():
    num = 0
    print("开始运行......")
    for i in range(0, 271, 30):
        print(i)
        page_url = start_url + str(i)
        get_url(page_url)
        print("okk...")
        time.sleep(2)
    print("链接获取完毕，开始下载...")
    for url in url_list:
        download_pic(url, num)
        num += 1
        if num % 10 == 0:
            print(f"已下载{num}张图片")
            time.sleep(1)


if __name__ == "__main__":
    main()
