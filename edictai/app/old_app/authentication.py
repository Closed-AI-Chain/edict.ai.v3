import requests
from scraper import title

title1 = title
url = "https://chatgpt-4-bing-ai-chat-api.p.rapidapi.com/chatgpt-4-bing-ai-chat-api/0.2/send-message/"

payload = f"bing_u_cookie=1pmI7w_INw4Gy852Hzqt4sDy8PZmBVtgC8FsN96KQl3PIUXoAY-24zmlGx9cDtc-C1j5u_5WJooRfc8gnHHApa_nkEwslZ0vq0hR8RIsxk8ytxZNpac9wp4KKybgMkQxGdUi4s8bUoD_yAocbUw9yYgzkwzHParkvAjdgPrvHI2Hl33-sCssW3796Kh3U9S1rk2xfIHvXIOBe0lGg0NxRMBxs70PYRgn5R0ytFFk_5Ac&question={title1} Is this a fake news? Answer 'Yes' or 'No' only"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e",
	"X-RapidAPI-Host": "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)