    
import requests
from bs4 import BeautifulSoup

def get_imdb(url, op , num):
    code = requests.get(url)
    text = code.text
    soup = BeautifulSoup(text, "html.parser")  
    
    list=""
    if op == 1:
        list += "\n Top " + str(num) + " Movies on IMDB are :- \n\n" 
    elif op == 2:
        list += "\n Top " + str(num) + " TV Shows on IMDB are :- \n\n" 
    i = 0    
    tbody = soup.find('tbody', {'class': 'lister-list'})
    for link in tbody.findAll('tr'):
        i += 1
        if i > num :
            break
        td_title = link.find('td', {'class': 'titleColumn'})
        title = td_title.find('a').string
        href = "https://www.imdb.com/" + td_title.find('a')['href']
        year = td_title.find('span').string
        
        td_rating = link.find('td', {'class': 'ratingColumn imdbRating'})
        rating = td_rating.find('strong').string
        
        list +=" " + str(i) + ". " + title + " " + year + "\n\tIMDB Rating => " +  rating + "\n\tLink => " + href + "\n\n"
        
            
    fw = open('IMDB.txt', 'w')
    fw.write(list)
    fw.close()
    
    print("\nSuccess !!!")



op = int(input("Enter option: \n 1. Movies \n 2. TV Shows\n => "))
if op != 1 and op != 2 :
    print(" Invalid Option !!!")


if op == 1:
    num = int(input("Enter the length of list [MAX : 250] => "))
    get_imdb("https://www.imdb.com/chart/top/", op , num)
elif op == 2:
    num = int(input("Enter the length of list [MAX : 250] => "))
    get_imdb("https://www.imdb.com/chart/toptv/", op , num)
    
