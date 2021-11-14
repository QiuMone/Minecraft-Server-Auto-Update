from types import FrameType
from typing import Text
from bs4.element import TemplateString
import requests
from bs4 import BeautifulSoup
import time
import schedule

def mc():
    print('查询中......')
    url1 = 'https://minecraft.fandom.com/zh/wiki/Java%E7%89%88'
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    rv = soup1.select('#mw-content-text > div > div.notaninfobox > table > tbody > tr:nth-child(4) > td > p > a:nth-child(2)')
    for r in rv:
        r = r.text
        print('正式版最新版本为 ' + r)
    sv = soup1.select('#mw-content-text > div > div.notaninfobox > table > tbody > tr:nth-child(4) > td > p > a:nth-child(5)')
    for s in sv:
        s = s.text
        print('快照版最新版本为 ' + s)
    url2 = 'https://minecraft.fandom.com/zh/wiki/Java%E7%89%88' + r
    #url3 = 'https://minecraft.fandom.com/zh/wiki/Java%E7%89%88' + s.text
    response2 = requests.get(url2)
    #response3 = requests.get(url3)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    #soup3 = BeautifulSoup(response3.text, 'html.parser')
    jj = soup2.select('#mw-content-text > div > p')
    dz = soup2.select('#mw-content-text > div > div.notaninfobox > table > tbody > tr:nth-child(4) > td > p > a:nth-child(4)')
    for jj in jj:
        print(jj.text)
    for d in dz:
        d = d['href']
    print(d)

    def downloadFile(name, url):
        headers = {'Proxy-Connection':'keep-alive'}
        r = requests.get(url, stream=True, headers=headers)
        length = float(r.headers['content-length'])
        f = open(name, 'wb')
        count = 0
        count_tmp = 0
        time1 = time.time()
        for chunk in r.iter_content(chunk_size = 512):
            if chunk:
                f.write(chunk)
                count += len(chunk)
                if time.time() - time1 > 2:
                    p = count / length * 100
                    speed = (count - count_tmp) / 1024 / 1024 / 2
                    count_tmp = count
                    print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                    time1 = time.time()
        f.close()
    
    def formatFloat(num):
        return '{:.2f}'.format(num)
    
    if __name__ == '__main__':
        downloadFile(r + '.jar', d)
mc()
