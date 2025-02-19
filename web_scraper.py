import bs4.element
import requests
from bs4 import BeautifulSoup

def scrape(url):
    data = requests.get(url)
    if data.status_code != 200:
        print("Error while trying to get data from " + url + ". Status code: " + str(data.status_code))
        return

    soup = BeautifulSoup(data.content, 'html.parser')

    p = soup.find_all('p', class_='body-graf')

    sentences = []
    for words in p:
        text = words.get_text()

        for sentence in text.split(','):
            cleaned_sentence = sentence.strip()
            if cleaned_sentence:
                sentences.append(cleaned_sentence)
                if len(sentences) >= 200:
                    break

    return sentences

url = 'https://www.nbcnews.com/politics/doge/doge-days-musk-trump-tout-cuts-fraud-claims-are-debunked-rcna192217'
sentences = scrape(url=url)
if sentences:
    for sentence in sentences:
        print(sentence)

print(len(sentences))