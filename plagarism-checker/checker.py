import requests
from bs4 import BeautifulSoup

class FilterOutData:
    def __init__(self):
        self._links = []
    def gethref(self,links):
        for l in soup.find_all('a',class_="result__url",href=True):
            self._links.append(l)
        return self
    def getContent(self):
        pass

class ChunkText:
    def __init__(self,text):
        self.text = text
        chunkList = text.split(".")
        print(chunkList)
class SendRequest:
    def __init__(self,url,chunk):
        URL = url
        params = {'q':chunk}
        headers = {
            'User-Agent':'Mozilla/5.0'
        }
        self.response= requests.post(URL,data=params,headers=headers)
    def getResult(self):
        return self.response.content
class Checker:
    def __init__(self,text):
       URL = "https://html.duckduckgo.com/html/"
       result = SendRequest(URL,text).getResult()

       soup = BeautifulSoup(result,'html.parser')
      
       anchors = soup.find_all('a')
    #    url = anchors[3].get('href')
    #    urlResult = SendRequest(url,'').getResult()
    #    print(BeautifulSoup(urlResult,"html.parser"))
       for i,a in enumerate(anchors,1):
           link = a.get('href')
           content = a.get_text(strip=True)
           if content is None:
               return 
           print(f"link: {link}, content:{content} ")
           print('\n')
      
      
Checker("It's no secret that India is a treasure trove of history, culture, and architecture, with some truly spectacular sights dotted throughout the vastcountry. As one of the most populous countries on earth with a huge land mass, India certainly has plenty on offer for every type of traveler. ")
#SendRequest("India is beautiful country")


