from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from newsapi import NewsApiClient
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import os
import json

def hindustan_times_single(url):

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    # accessing the contents or url
    driver.get(url)

    # scraping the title of article
    title = driver.find_element(By.XPATH, '//h1[@class="hdg1"]' ).text

    # scraping publishing data of article
    published_on = driver.find_element(By.XPATH, '//div[@class="actionDiv flexElm topTime"]' ).text

    # scraping all text from the article
    scraped_content = driver.find_element(By.XPATH, '//h2[@class="sortDec"]' ).text

    p_tags = driver.find_elements(By.TAG_NAME,'p')

    for i in p_tags:
        scraped_content += i.text

    # scraping images

    image_urls = driver.find_elements(By.XPATH, '//figure/span/picture/img')

    images_data = []

    for i in image_urls:
        img_url = i.get_attribute("src")
        images_data.append(img_url)

    driver.quit()

    data = {"headline" : title,
            "content":scraped_content,
            "published_on": published_on[:len(published_on)-29],
            "image_urls" : images_data
    }
    
    # data = {"headline": "", "subheadline": "", "content": "", "image_path": ""} 
    return(data)  

def coindesk_multiple():

    import requests
    from bs4 import BeautifulSoup

    url = "https://crypto-news16.p.rapidapi.com/news/coindesk"
    data = []

    headers = {
        "X-RapidAPI-Key": "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e",
        "X-RapidAPI-Host": "crypto-news16.p.rapidapi.com"
    }

    response_coindesk = requests.request("GET", url, headers=headers)

    for i in range(3,10):

        url = response_coindesk.json()[i]['url']

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        media_div = soup.find('div', class_='media')
        if media_div:
            image_urls = [img['src'] for img in media_div.find_all('img')]
            for j, url in enumerate(image_urls):
                img_data = requests.get(url).content
                file_extension = url.split(".")[-1]
                if file_extension in ['jpg', 'jpeg', 'png']:
                    image_path = f"images/coindesk_multiple_{i}.{file_extension}"
                    i += 1
                if response.status_code == 200:
                    headline = soup.find('div', class_='at-headline').find('h1').get_text().strip()
                    subheadline = soup.find('div', class_='at-subheadline').find('h2').get_text().strip()
                    content_div = soup.find('div', class_='at-content-wrapper')
                    content = ' '.join([p.get_text().strip() for p in content_div.find_all('p')])
                else:
                    print("Request failed with status code:", response.status_code)
                    with open(image_path, "wb") as f:
                        f.write(img_data)
            single_data = {
                    "headline": headline,
                    "subheadline": subheadline,
                    "content": content, 
                    "image_path": image_path
                }

            data.append(single_data)
            
        else:
            image_path = ""
            print("No images found.")
        

    # data = [{"headline": "", "subheadline": "", "content": "", "image_path": ""},{},{},....]
    return(data) 

def coindesk_single(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headline = soup.find('div', class_='at-headline').find('h1').get_text().strip()
        subheadline = soup.find('div', class_='at-subheadline').find('h2').get_text().strip()
        content_div = soup.find('div', class_='at-content-wrapper')
        content = ' '.join([p.get_text().strip() for p in content_div.find_all('p')])
    else:
        print("Request failed with status code:", response.status_code)

    media_div = soup.find('div', class_='media')
    if media_div:
        image_urls = [img['src'] for img in media_div.find_all('img')]
        for j, url in enumerate(image_urls):
            img_data = requests.get(url).content
            file_extension = url.split(".")[-1]
            image_path = f"images/coindesk_single_{j}.{file_extension}"
            if file_extension in ['jpg', 'jpeg', 'png']:
                with open(image_path, "wb") as f:
                    f.write(img_data)
    else:
        media_div = soup.find('div', class_='at-img')
        if media_div:
            image_urls = [img['src'] for img in media_div.find_all('img')]
            for j, url in enumerate(image_urls):
                img_data = requests.get(url).content
                file_extension = url.split(".")[-1]
                image_path = f"images/coindesk_single_{j}.{file_extension}"
                if file_extension in ['jpg', 'jpeg', 'png']:
                    with open(image_path, "wb") as f:
                        f.write(img_data)
        else:
            image_path = ""
            print("No images found.")

    data = {
        "headline": headline,
        "subheadline": subheadline,
        "content": content,
    }

    return(data) 

def toi_election_multiple():

    url = 'https://timesofindia.indiatimes.com/elections'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []

    for span in soup.find_all('span', class_='w_tle'):
        for a in span.find_all('a'):
            href = a.get('href')
            text = a.text.strip()
            results.append(href)

    for i in range(len(results)):
        results[i] = "https://timesofindia.indiatimes.com/elections" + str(results[i])

    data = []
    k = 0 

    for i in range(len(results)):

        url = results[i]

        response = requests.get(url)

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            headline = text = soup.find("h1", class_="HNMDR").get_text(strip=True)
            content = " ".join([div.get_text(strip=True) for div in soup.find_all("div", class_="_s30J clearfix")])
        except:
            print("Request failed with status code:", response.status_code)

        i += 1

        try:
            media_div = soup.find('div', class_='wJnIp')
            image_urls = [img['src'] for img in media_div.find_all('img')]
            for j, url in enumerate(image_urls):
                img_data = requests.get(url).content
                file_extension = url.split(".")[-1]
                image_path = f"images/toi_elections_{k+1}.{file_extension}"
                if file_extension in ['jpg', 'jpeg', 'png']:
                    with open(image_path, "wb") as f:
                        f.write(img_data)
            if(headline!="" and content!="" and len(image_urls)!=0):
              single_data = {
                  "headline": headline,
                  "content": content,
                  "image_path": image_path
              }
              data.append(single_data)
              k+=1
            if(k>=5):
              break
        except: 
            print("No images found.")

    return(data)

def the_hindu_single(url):

    getData = requests.get(url)
    getHtml = BeautifulSoup(getData.content, "html.parser")

    # scraping the title of article
    title = getHtml.find("h1", {"class" :"title"}).getText().replace("\n", "").replace("\\", "")

    subtitle = getHtml.find('h3', {"class" : "sub-title"}).getText().replace("\n", "").replace("\\", "")

    scraped_content = ""

    div = getHtml.find("div", {"class" : "articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12"})

    # (Byfind.XPATH,'//div[@class="articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12"]/p')

    p_tags = div.findAll("p")

    for i in p_tags:
        scraped_content += i.getText()
        
    ind = scraped_content.find("COMMents")
    scraped_content = scraped_content[:ind]

    scraped_content = scraped_content.replace("\n", "").replace("\\", "")

    # scraping images

    image_url = getHtml.find("img", {"class" : "lead-img"})["src"]

    data = {
        "headline" :title,
        "subheadline" : subtitle,
        "content" : scraped_content
    }

    return(data)

def the_hindu_multiple():

    # Make a request to the webpage
    url = "https://www.thehindu.com/latest-news/"
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <div> with class "col-xl-6 col-lg-8 col-md-8 col-sm-12 col-12 latest-news"
    latest_news_div = soup.find('div', class_='col-xl-6 col-lg-8 col-md-8 col-sm-12 col-12 latest-news')

    # Find all <a> tags within the <div> and extract their URLs and text
    a_tags = latest_news_div.find_all('a')

    i=0
    data = []

    for a_tag in a_tags:
        try:
            url = a_tag['href']
            try:
                single_data = the_hindu_single(url)
                i += 1
                if(i%2==0):
                    data.append(single_data)
                if(i>10):
                    break
            except:
                pass 
        except:
            pass
    
    return(data)

def ndtv_single(url):

    getData = requests.get(url)
    getHtml = BeautifulSoup(getData.content, "html.parser")

    # scraping the title of article
    title = getHtml.find("h1", {"class" :"sp-ttl"}).getText()

    subtitle =""
    try:
        subtitle = getHtml.find('h3', {"class" : "sp-descp"}).getText()
    except Exception as e:
        pass

    scraped_content = ""

    div = getHtml.find("div", {"class" : "sp-cn ins_storybody"})

    # (Byfind.XPATH,'//div[@class="articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12"]/p')

    p_tags = div.findAll("p")

    for i in p_tags:
        scraped_content += i.getText()+" "

    data = {
        "headline" :title,
        "subheadline" : subtitle,
        "content" : scraped_content,
    }

    return(data)

def ndtv_multiple_latest():
    # Make a request to the webpage
    url = "https://www.ndtv.com/latest"
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags with class "news_Itm-img"
    news_itm_imgs = soup.find_all('div', class_='news_Itm-img')

    i = 0
    data = []

    # Extract links from each <div>
    for news_itm_img in news_itm_imgs:
        link_tag = news_itm_img.find('a')
        link = link_tag['href']
        try:
            single_data = ndtv_single(link)
            i+=1
            data.append(single_data)
            if(i>5):
                break
        except:
            pass
    
    return(data)

def ndtv_multiple_india():
    # Make a request to the webpage
    url = "https://www.ndtv.com/india"
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags with class "news_Itm-img"
    news_itm_imgs = soup.find_all('div', class_='news_Itm-img')

    i = 0
    data = []

    # Extract links from each <div>
    for news_itm_img in news_itm_imgs:
        link_tag = news_itm_img.find('a')
        link = link_tag['href']
        try:
            single_data = ndtv_single(link)
            i+=1
            data.append(single_data)
            if(i>5):
                break
        except:
            pass
    
    return(data)

def news_api():
    print("Sources: ")
    # Init
    newsapi = NewsApiClient(api_key='efa6c22c503841b8944239d165f3a32c')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q=query,
                                            # sources='bbc-news,the-verge',
                                            # category='business',
                                            language='en',
                                            # country='in'
                                            )

    # /v2/everything
    all_articles = newsapi.get_everything(q='bitcoin',
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param='2017-12-01',
                                        to='2017-12-12',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()    

def url_select(url):

    if("https://www.hindustantimes.com/" in url):
        data = hindustan_times_single(url)

    elif("https://www.coindesk.com/" in url):
        if(url=="https://www.coindesk.com/" or url=="https://www.coindesk.com/tag/news/" or url=="https://www.coindesk.com/markets/" or url=="https://www.coindesk.com/tv/breaking-news/" or url=="https://www.coindesk.com/company-news/" or url=="https://www.coindesk.com/policy/" or url=="https://www.coindesk.com/tech/" or url=="https://www.coindesk.com/web3/" ):
            data = coindesk_multiple()
        else:
            data = coindesk_single(url)

    elif("https://timesofindia.indiatimes.com/" in url):
        if(url=="https://timesofindia.indiatimes.com/" or url=="https://timesofindia.indiatimes.com/elections"):
            data = toi_election_multiple()
            
    elif("https://www.thehindu.com/" in url):
        if(url=="https://www.thehindu.com/" or url=="https://www.thehindu.com/news/national/" or url=="https://www.thehindu.com/news/" or url=="https://www.thehindu.com/news/international/" or url=="https://www.thehindu.com/news/states/" or url=="https://www.thehindu.com/news/cities/"):
            data = the_hindu_multiple()
        else:
            data = the_hindu_single(url)

    elif("https://www.ndtv.com/" in url):
        if(url == "https://www.ndtv.com/" or url=="https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation" or url=="https://www.ndtv.com/latest"):
            data = ndtv_multiple_latest()
        elif(url=="https://www.ndtv.com/india" or url=="https://www.ndtv.com/elections"):
            data = ndtv_multiple_india()
        else:
            data = ndtv_single(url)

    return(data)

def url_identify(url):

    if("https://www.hindustantimes.com/" in url):
        data = "single"

    elif("https://www.coindesk.com/" in url):
        if(url=="https://www.coindesk.com/" or url=="https://www.coindesk.com/tag/news/" or url=="https://www.coindesk.com/markets/" or url=="https://www.coindesk.com/tv/breaking-news/" or url=="https://www.coindesk.com/company-news/" or url=="https://www.coindesk.com/policy/" or url=="https://www.coindesk.com/tech/" or url=="https://www.coindesk.com/web3/" ):
            data = "multiple"
        else:
            data = "single"

    elif("https://timesofindia.indiatimes.com/" in url):
        if(url=="https://timesofindia.indiatimes.com/" or url=="https://timesofindia.indiatimes.com/elections"):
            data = "multiple"
            
    elif("https://www.thehindu.com/" in url):
        if(url=="https://www.thehindu.com/" or url=="https://www.thehindu.com/news/national/" or url=="https://www.thehindu.com/news/" or url=="https://www.thehindu.com/news/international/" or url=="https://www.thehindu.com/news/states/" or url=="https://www.thehindu.com/news/cities/"):
            data = "multiple"
        else:
            data = "single"

    elif("https://www.ndtv.com/" in url):
        if(url == "https://www.ndtv.com/" or url=="https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation" or url=="https://www.ndtv.com/latest"):
            data = "multiple"
        elif(url=="https://www.ndtv.com/india" or url=="https://www.ndtv.com/elections"):
            data = "multiple"
        else:
            data = "single"

    return(data)
