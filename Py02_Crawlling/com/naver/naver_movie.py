# pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request

# urllib.request : 해당 url의 데이터를 가져온다
# beautifulsoup : parsing 해줌

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)
#print(soup.findAll('dt',{'class','tit'}))
movieList = soup.findAll('dl',{'class','lst_dsc'})
for movieOne in movieList :
    link = movieOne.find('a').text
    star = movieOne.find('span',{'class','num'}).text
    #print(link)
    #print(star)
    print('{"name":"%s", "star":"%s"}' % (link, star))
