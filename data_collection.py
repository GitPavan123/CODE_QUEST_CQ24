import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        
        content = '\n'.join([p.get_text() for p in paragraphs])
        return content
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

url = "https://en.wikipedia.org/wiki/Java_(programming_language)"
webpage_content = scrape_webpage(url)
if webpage_content:
    print("Content from the webpage:")
    print(webpage_content)



def fembedding_lauer(pARAM):
    use = 
