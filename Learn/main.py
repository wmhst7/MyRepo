import sys
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
for each in soup.find_all('div', class_='info'):
    img_url = each.previous_sibling.previous_sibling.a.img['src']
    title = each.find('div', class_='hd').get_text(strip=True).replace('\xa0','').split('/',1)[0]
    #print('title:',title)
    #print(each.a.attrs['href'])
    #print(each.find('div', class_='bd').p.get_text().replace('导演:',''))
    #name = title.split('/', 1)[0]#打印图片到本地
    # with open(name+'_img.jpg', 'wb') as img:
    #     #img.write(requests.get(img_url).content)
    actor = list(each.find('p', class_='').strings)[0].strip().replace('\xa0','')
    type_list = list(each.find('p').strings)[1].strip().replace('\xa0','').split('/')
    year = type_list[0]
    country = type_list[1]
    type_ = type_list[2]
    star = each.find('span', class_='rating_num').get_text(strip=True)
    print(title,'\n'+year,country,type_,star,actor)
