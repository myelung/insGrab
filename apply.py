from bs4 import BeautifulSoup
from lxml import html
import xml
import urllib.request as urlrequest
import requests
from wsgiref.simple_server import make_server



def getContentDisplay():

    timeOfParas = 3
    conStr = "<!DOCTYPE html><meta charset = \"utf-8\"><html><title></title><head>ALL I GOT FOR YOU FROM IT199</head>"
    conStr += "<body>"

    endStr = "</body></html>"
    
    url = "https://www.199it.com"
    f = requests.get(url)
    page = urlrequest.urlopen(url).read()
    soup = BeautifulSoup(f.content, "lxml")

    for k in soup.find_all('h2', class_ = 'entry-title'):
        #every h2 with potential class
        aa = k.find_all('a')
        #aaa = aa.find_all('href')
        print(aa[0].string)
        aaaa = ""
        aaaa = aa[0].get('href')
        aTitle = aa[0].get('title')

        '''
        for aaa in aa:
            aaaa = aaa.get('href')
            aTitle = aaa.get('title')
            print("\n++++++++\n" + aTitle + "\n++++++++\n")
            #print(aaaa)
        '''
        #print(aaaa)
        

        '''
            So now what we have here is the title and the website.
        '''
        urlOfEachArticle = aaaa
        articleContent = requests.get(urlOfEachArticle)
        articleSoup = BeautifulSoup(articleContent.content, "lxml")
        for paras in articleSoup.find_all('div', class_ = "entry-content articlebody"):
            paraContent = paras.find_all('p')
            if (paraContent[0].string is not None):
                #conStr += "<h2>"
                if (aa[0].string != ""):
                    conStr += "<h2><a href = \"" + aaaa + "\">" + aa[0].string + "</a>"
                    conStr += "</h2><br>"
                elif (aTitle.string != ""):
                    conStr += "<h2><a href = \"" + aaaa + "\">" + aTitle + "</a>"
                    conStr += "</h2><br>"

                for para in paraContent:
                    if (para.string is not None and para.string != ""):
                        conStr += "<p>" + para.string + "</p>"
            '''
            if (paraContent[0] != None):
                print(paraContent[0].string)
                if (paraContent[0].string is None):
                    pass
                else:
                    conStr += "<h2>"
                    conStr += "<a href = \"" + aaaa + "\">" + aa[0].string + "</a>"
                    
                    conStr += "<p>" + (paraContent[0].string) + "</p>"
                    conStr += "<br>**********************************<br>"
            '''

        #print("\n**********************************\n")
    conStr += endStr
    return conStr

def applier(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #return [b'<h1>How Are You!</h1><h2>What if we called?</h2>']
    #return bytes(getContentDisplay(), encoding = 'utf8')
    getCon = getContentDisplay()
    #getCon = "AAA"
    #print(type([b'po']))
    print("\n\n\n\n")
    if (type(getCon.encode()) is '''bytes'''):
        print("*****\n\n\n\n\n\n" + getCon + "\n**************\n")
    getConList = [getCon.encode()]
    return getConList

a = 900
httpd = make_server('', a, applier)

httpd.serve_forever()

