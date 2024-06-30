import requests
from bs4 import BeautifulSoup
import sys

def horoscopeTeller(zodiacSign):
    
    zodiacSignsMap = {'aries':1, 'taurus':2, 'gemini':3, 'cancer':4, 'leo':5, 'virgo':6, 'libra':7, 'scorpio':8, 'sagittarius':9, 'capricorn':10, 'aquarius':11, 'pisces':12}
    astrologyWebSite = requests.get('https://www.horoscope.com')
    
    parser = BeautifulSoup(astrologyWebSite.content, 'html5lib')
    
    zodiacSignsList = parser.find('div', class_ = 'grid grid-6')
    
    
    horoscopeLink = zodiacSignsList.find_all('a')[zodiacSignsMap[zodiacSign]-1]['href']

    joinedUrl = 'https://www.horoscope.com' + horoscopeLink
    signWebPage = requests.get(joinedUrl)
    signParser = BeautifulSoup(signWebPage.content, 'html5lib')
    fortune = signParser.find('div', class_ = 'main-horoscope')
    print(fortune.p.text)

if __name__ == '__main__':
    try:
        horoscopeTeller(sys.argv[1])
    except:
        print("please enter a valid zodiac sign ...")
