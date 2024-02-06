import requests
from bs4 import BeautifulSoup

SOURCE_WEBSITE_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(SOURCE_WEBSITE_URL)
# print(response.text)
response_text = response.text
dict = {}
soup = BeautifulSoup(response_text, "html.parser")
raw_data = soup.select(selector=".listicle_listicle__item__CJna4 h3.listicleItem_listicle-item__title__BfenH")
data = [title.getText() for title in raw_data][::-1]
with open("100BestMovie.txt", 'w', newline='') as file:
    for movie in data:
        file.write(f"{movie}\n")
print(data)
