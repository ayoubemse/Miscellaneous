import requests
from http.client import HTTPConnection
from urllib.parse import urlparse
import sched, time
import smtplib
from datetime import datetime


scheduler = sched.scheduler(time.time,
                            time.sleep)
def connectedToInternet():
    
    try:
        requests.get('http://www.google.com')
        requests.get("https://linkedin.com")
        return True
    except:
        return False


def checkWebSite(url, tiemout = 2):
    
    
    if not connectedToInternet():
        print("cannot connect to internet. please check your connectivity and try again...")
        return False
    else:
        
        error = Exception("website is down !")
        urlParse = urlparse(url)
        urlHostname = urlParse.hostname
        
        http_port = 80
        https_port = 443
        for port in (http_port, https_port):
            connect = HTTPConnection(host=urlHostname, port= port, timeout=tiemout)
            try:
                connect.request('HEAD', '/')
                return True
            except Exception as e:
                error = e
                return False
            finally:
                connect.close()
        raise error


def sendEmailAlert(destination_email):
    
    message = "site is up and running !\n"
    senderEmail = 'senderpython97@gmail.com'
    appPassword = os.getenv('EMAIL_APP_PASSWORD')
    if appPassword is None:
        raise ValueError("No password found in environment variables")
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(senderEmail, appPassword)
        server.sendmail('senderpython97@gmail.com', destination_email, message)
        server.quit()



def runCheckingWebSite(url, destinationEmail):
    if not connectedToInternet():
        print("check your internet connectivity and retry..")
        return
    else:
        if checkWebSite(url):
            sendEmailAlert(destinationEmail)


def siteChecker(schedlr, destinationEmail, url):
    
        schedlr.enter(5, 1, runCheckingWebSite, (url, destinationEmail))
        


siteChecker(scheduler, 'touibiayoub@gmail.com', 'https://www.blsspainmorocco.net/mar/home/index')
scheduler.run()
        
