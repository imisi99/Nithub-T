import requests
from bs4 import BeautifulSoup

def scrape(url):
    data = requests.get(url)
    if data.status_code != 200:
        print("Error while trying to get data from " + url + ". Status code: " + str(data.status_code))
        return

    soup = BeautifulSoup(data.content, 'html.parser')

    # T1 p = soup.find_all('p', class_='body-graf')
    p = soup.find_all('p', class_='dcr-s3ycb2')

    sentences = []
    for words in p:
        text = words.get_text()

        for sentence in text.split('.'):
            cleaned_sentence = sentence.strip()
            if cleaned_sentence:
                sentences.append(cleaned_sentence)
                if len(sentences) >= 200:
                    break

    return sentences

# T1 url = 'https://www.nbcnews.com/politics/doge/doge-days-musk-trump-tout-cuts-fraud-claims-are-debunked-rcna192217'
url = 'https://www.theguardian.com/commentisfree/2024/nov/04/ipp-sentences-labour-england-wales-prisons'
sentences = scrape(url=url)
if sentences:
    for sentence in sentences:
        print(sentence)

print(len(sentences))