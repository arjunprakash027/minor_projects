from requests.api import request
import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import time
import smtplib
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
def price_find():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Time: ",current_time)
  print("Connecting to amazon...")
  URL = 'https://www.amazon.in/boAt-Airdopes-141-Wireless-Resistance/dp/B09N3ZNHTY/ref=asc_df_B09N3ZNHTY/?tag=googleshopdes-21&linkCode=df0&hvadid=545088051503&hvpos=&hvnetw=g&hvrand=15664384979627146403&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061935&hvtargid=pla-1625292053964&th=1'
  r = requests.get(URL,headers=HEADERS)
  soup = BeautifulSoup(r.content,'lxml')
  price = soup.select('#corePrice_feature_div span')[0].get_text()
  price = price.replace('.', '')
  price = price.replace(',','.')
  price_format = float(price[1:6])
  print(price_format)
  if(price_format < 1.299):
     send_mail()

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('aiarjun027@gmail.com','password')

  subject = 'price fell down!!!!'
  body ='check the link https://www.amazon.in/boAt-Airdopes-141-Wireless-Resistance/dp/B09N3ZNHTY/ref=asc_df_B09N3ZNHTY/?tag=googleshopdes-21&linkCode=df0&hvadid=545088051503&hvpos=&hvnetw=g&hvrand=15664384979627146403&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061935&hvtargid=pla-1625292053964&th=1'
  
  msg = f"Subject : {subject}\n\n{body}"

  server.sendmail(
      'aiarjun027@gmail.com',
      'arjunprakash027@gmail.com',
      msg
  )
  print('email sent')

  server.quit()

price_find()
