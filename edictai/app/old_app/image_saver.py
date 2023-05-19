from scraper import data
import os
import urllib.request

def download_images(urls, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, url in enumerate(urls):
        try:
            file_name = os.path.join(folder, f"image_{i}.jpg")
            urllib.request.urlretrieve(url, file_name)
            print(f"{url} - downloaded")
        except Exception as e:
            print(f"{url} - {e}")

# Example usage:
urls = ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
urls.append[data.image_urls]
folder = "images"
download_images(urls, folder)
