import requests, openpyxl
from bs4 import BeautifulSoup
excel =openpyxl.Workbook()
sheet = excel.active
sheet.title ='movies'
try:
    url =requests.get('https://www.cnet.com/news/netflix-39-of-the-absolute-best-movies-to-watch-this-weekend/')
    url.raise_for_status()
    soup = BeautifulSoup(url.content,'html.parser')
    movies = soup.findAll('h2')
    i =1
    q=1
    k=1
    j=3
    for movie in movies:
        name= movie.text
        if len(name.split()) ==1:

            q = i
            sheet.cell(row =j, column =i).value =name
            k=4
            i =i+1
            #sheet.append([s])
        if len(s.split()) >=2:

            sheet.cell(row=k, column=q).value =name
            k=k+1
            #sheet.append([s])

except Exception as e:
     print(e)
excel.save("movies9.xlsx")

'''category = soup.find('div',class_ ='col-7 article-main-body row')
cc= category.findAll('div',class_ = 'shortcode listicle')
for i in cc:
   print( i.find('h2').text)'''










