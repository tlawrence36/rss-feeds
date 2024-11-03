import feedparser
import requests
from bs4 import BeautifulSoup
import json

feed_list = [] # list of feeds
parsed_articles = [] # articles from feeds
content = [] # JSON of all content

def fetch_feeds_list(): # use filename param?
    print('get list of feeds to use')
    # get list of names to use
    with open("feeds.txt") as feeds_file:
        feeds = feeds_file.readlines()
        for feed in feeds:
            feed_info = feed.replace('\n', '').split(',')
            # print(feed_info)
            feed_list.append(feed_info)

def parse_rss_feeds():
    print('parse feeds to get articles')
    for feed in feed_list:
        theFeed = feedparser.parse(feed[2])
        for entry in theFeed.entries:
            item = {
                "source": feed[0],
                "category": feed[1],
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary
            }
            parsed_articles.append(item)

def get_container(soup, source):
    if source == 'ABC':
        return soup.find('div', class_='FITT_Article_main__body')
    elif source == 'BBC':
        return soup.find('article')
    elif source == 'CBS':
        return soup.find('section', class_='content__body')
    elif source == 'FOX':
        return soup.find('div', class_='article-body')
    elif source == 'HuffPost':
        return soup.find('section', class_='entry__content-list')
    elif source == 'NBC':
        return soup.find('div', class_='article-body__content')

def scrape_articles():
    print('scrape articles, save to JSON for astro')
    article_id = 1
    for article in parsed_articles:
        if article['link'].find('video') == -1:
            # print(article['link'])
            response = requests.get(article['link'])#
            soup = BeautifulSoup(response.content, 'html.parser')
            container = get_container(soup, article['source'])

            if container is not None:
                item = {
                    "id": article_id,
                    "source": article['source'],
                    "category": article['category'],
                    "title": article['title'],
                    "published": article['published'],
                    "summary": article['summary'],
                }

                lines = container.find_all(["p", "h2", "ul", "li"])
                story = []
                for line in lines:
                    if line.text is not '':
                        story.append(line.text.strip())
                item['story'] = story
                content.append(item)
                article_id += 1

    json_content = json.dumps(content, indent=2)
    with open("feed.json", "w", encoding="utf-8") as f:
        f.write(json_content)

if __name__ == "__main__":
    fetch_feeds_list()
    parse_rss_feeds()
    scrape_articles()