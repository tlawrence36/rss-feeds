import feedparser
import requests
from bs4 import BeautifulSoup
import json
import datetime

feed_list = [] # list of feeds
parsed_articles = [] # articles from feeds
content = [] # JSON of all content

def filter_period(period, date_str):
    month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    parts = date_str.split()
    article_date = datetime.date(int(parts[3]), month_map[parts[2]], int(parts[1]))
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=period)
    return article_date > week_ago

def fetch_feeds_list(): # use filename param?
    print('get list of feeds to use')
    # get list of names to use
    with open("feed/feeds.txt") as feeds_file:
        feeds = feeds_file.readlines()
        for feed in feeds:
            feed_info = feed.replace('\n', '').split(',')
            # print(feed_info)
            feed_list.append(feed_info)

def parse_rss_feeds():
    print('parse feeds to get articles')
    for feed in feed_list:
        the_feed = feedparser.parse(feed[2])
        for entry in the_feed.entries:
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
        # only include articles from the past 7 days
        if filter_period(7, article['published']):
            if article['link'].find('video') == -1:
                # print(article['link'])
                response = requests.get(article['link'])
                if response:
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
                            if line.text != '':
                                story.append(line.text.strip())
                        item['story'] = story
                        content.append(item)
                        article_id += 1

    # print(content)
    json_content = json.dumps(content, indent=2)
    with open("feed.json", "w", encoding="utf-8") as f:
        f.write(json_content)

if __name__ == "__main__":
    fetch_feeds_list()
    parse_rss_feeds()
    scrape_articles()