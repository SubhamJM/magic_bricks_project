from bs4 import BeautifulSoup

d = {}
i = 0
data = open('magic_bricks_project/data.html','r').read()

soup = BeautifulSoup(data,'lxml')
elems = soup.select('div.mb-srp__list')
for elem in elems:
    title = elem.select_one('h2.mb-srp__card--title').text
    try:
        residency = elem.select_one('span.mb-srp__card__developer--name--highlight').text
    except:
        residency = 'none'
    price = elem.select_one('div.mb-srp__card__price--amount').text.replace('â‚¹','Rs ')
    area = elem.select_one('div.mb-srp__card__summary--value').text
    ready = ' '.join(elem.select('div.mb-srp__card__summary--value')[1].text.split()[-2:])
    try:
        link = elem.select_one('a.mb-srp__card__society--name').get('href')
    except:
        link = 'no link'
    
    d[i] = [title,residency,price,area,ready,link]
    i += 1

with open('magic_bricks_project/result.csv','w',encoding='utf-8',newline='') as file:
    import csv
    writer = csv.writer(file)
    writer.writerow(['title','scoiety','price','area','when ready','link'])
    for i in d:
        writer.writerow(d[i])