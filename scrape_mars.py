

from splinter import Browser
from bs4 import BeautifulSoup as bs
import os
from requests import get
import requests
import pandas as pd


def init_browser():

    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()

    mars_info={}


    mars=requests.get('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')





    print(mars.text)


    soup=bs(mars.text, 'html.parser')



    news_title=soup.find('div', 'content_title', 'div').text.strip()
    print(news_title)





    news_paragraph=soup.find('div', 'rollover_description_inner').text.strip()
    print(news_paragraph)



    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')




    html=browser.html
    soup=bs(html,'html.parser')





    image=soup.find("img", class_="thumb")["src"]
    featured_image_url="https://www.jpl.nasa.gov" + image
    print(featured_image_url)




    browser.visit('https://twitter.com/marswxreport?lang=en')





    html=browser.html
    soup=bs(html,'html.parser')




    tweet=soup.find('ol', class_='stream-items')
    mars_weather=tweet.find('p', class_='TweetTextSize').text.strip()
    print(mars_weather)





    url='https://space-facts.com/mars/'





    tables=pd.read_html(url)
    tables





    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


    html=browser.html
    soup=bs(html,'html.parser')





    hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_url=[]
    hemispheres=soup.find_all('div',class_="item")
    for hemisphere in hemispheres:
        hemisphere_dict={}
        title=hemisphere.find('h3').text.strip()
        hemisphere_dict["title"]= title
        partial_img_url=soup.find('a', class_= 'itemLink product-item')['href']
        hemisphere_html=browser.html
        soup=bs(hemisphere_html,'html.parser')
        img_link=soup.find('div',class_= 'downloads')
        hemisphere_dict["img_link"]= img_link
        hemisphere_image_url.append({"title": title, "img_link": img_link})



    hemisphere_image_url

    mars_info={
        "news title": news_title,
        "news paragraph": news_paragraph,
        "mars weather": mars_weather,
        "tables": tables,
        "hemisphere image": hemisphere_image_url

    }

    browser.quit()
    
    return mars_info