import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests_html import HTML,HTMLSession

with requests.Session() as s :
    session = HTMLSession()
    r = session.get('https://www.flipkart.com/search?q=televisions&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_3_0&otracker1=AS_Query_TrendingAutoSuggest_3_0&as-pos=3&as-type=TRENDING')
    soup = BeautifulSoup(r.content, 'html.parser')



containers = soup.find_all('div',{'class':'_1HmYoV _35HD7C'})

'''new = containers[0]

new = new.find_all('div',{'class':'bhgxx2'})

new1=new[0]
print(new1.div.div)'''

container = containers[0]

new = containers[1]

hello = new.find_all('div',{'class':'_1-2Iqu row'})

hi=hello[0]


#print(BeautifulSoup.prettify(hi))

ni = hi.find_all('div',{'class':'niH0FQ'})

y=ni[0]

#print(y.div.text)





#print(BeautifulSoup.prettify(new))


filename = "product.csv"

f=open(filename,"w")

headers="name,price\n"
f.write(headers)


arr=[]

import pandas as pd
for i in hello :
    lis=[]
    name = i.div.div.text
    ni = i.find_all('div',{'class':'col col-5-12 _2o7WAb'})
    fi = i.find_all('div',{'class':'niH0FQ'})
    x = ni[0]
    price = x.div.div.div.text.strip()
    lis.append(name)
    lis.append(price)
    arr.append(lis)


data = pd.DataFrame(arr,columns=["name","price"])

yes = data["name"]

print(yes.to_string(index=False))


#print(new.div.a.div.div.div.img["alt"])



