import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        return {'title': title, 'links': links}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    url = input("Enter the URL to scrape: ")
    result = scrape_website(url)
    print(result)