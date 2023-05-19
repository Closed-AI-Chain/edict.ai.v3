from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

def hindustanTimes(url):
    # url = "https://www.hindustantimes.com/cities/jaipur-news/sachin-pilot-announces-hunger-strike-against-rajasthan-govt-s-alleged-corruption-by-previous-bjp-tenure-101681030452310.html"

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
    print(image_urls)
    for i in image_urls:
        img_url = i.get_attribute("src")
        images_data.append(img_url)

    driver.quit()

    data = {"Title" : title,
            "Published ON": published_on[:len(published_on)-29],
            "Data":scraped_content,
            "Image_Urls" : images_data
    }
    print(title)
    return(scraped_content)  
# print(data['Image_Urls'])
def coinDesk():

    url = "https://crypto-news16.p.rapidapi.com/news/coindesk"

    headers = {
        "X-RapidAPI-Key": "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e",
        "X-RapidAPI-Host": "crypto-news16.p.rapidapi.com"
    }

    chunks = []

    response_coindesk = requests.request("GET", url, headers=headers)

    for i in range(5):

        single_chunk = []

        url = response_coindesk.json()[i]['url']

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            headline = soup.find('div', class_='at-headline').find('h1').get_text().strip()
            subheadline = soup.find('div', class_='at-subheadline').find('h2').get_text().strip()
            content_div = soup.find('div', class_='at-content-wrapper')
            content = ' '.join([p.get_text().strip() for p in content_div.find_all('p')])
            single_chunk.append("News "+str(i+1)+":"+subheadline)
        else:
            print("Request failed with status code:", response.status_code)

        i += 1

        media_div = soup.find('div', class_='media')
        if media_div:
            image_urls = [img['src'] for img in media_div.find_all('img')]
            for j, url in enumerate(image_urls):
                img_data = requests.get(url).content
                file_extension = url.split(".")[-1]
                if file_extension in ['jpg', 'jpeg', 'png']:
                    file_name = f"images/Coindesk_{i}_{j}.{file_extension}"
                    with open(file_name, "wb") as f:
                        f.write(img_data)
        else:
            print("No images found.")
        
        single_chunk.append(file_name)
        chunks.append(single_chunk)

    return chunks