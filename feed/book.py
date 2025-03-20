import httpx
from bs4 import BeautifulSoup

# content = []
pages = range(2,26)
with open("stripped.txt", 'a') as book:
    for page in pages:
        # url = f"https://jasinda-wilder.freenovelread.com/1615-stripped"
        url = f"https://jasinda-wilder.freenovelread.com/page,{page},1615-stripped"
        print(f"page: {page}")
        response = httpx.get(url)
        soup = BeautifulSoup(response, 'html.parser')
        page_content = soup.find("div", {"class": "content-center"}).text

        book.write(page_content)