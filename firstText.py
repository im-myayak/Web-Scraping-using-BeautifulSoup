from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
response_text = response.text
dict = {}
soup = BeautifulSoup(response_text, "html.parser")
title_rows = [title.find(name="a") for title in soup.select(selector="td span.titleline")]
news_score = soup.select(selector="td.subtext")

for index in range(len(title_rows)):
    title = title_rows[index].getText()
    link = title_rows[index].get("href")
    try:     score = int(news_score[index].find(name='span', class_='score').getText().split()[0])
    except AttributeError:   score = 0


    dict[title] = [score,link]

print(dict)


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())
# for tag in soup.find_all(name="a"):
#     print(tag.getText())
