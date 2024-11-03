import feedparser
import json

# Replace with your RSS feed URL
RSS_FEED_URL = "https://abcnews.go.com/abcnews/usheadlines"

def scrape_rss_feed():
    # Parse the RSS feed using feedparser
    feed = feedparser.parse(RSS_FEED_URL)

    # Initialize an empty list to store scraped items
    scraped_items = []

    # Iterate through each feed item
    for entry in feed.entries:
        item = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        }
        scraped_items.append(item)

    # Return the scraped items as a JSON object
    return json.dumps(scraped_items, indent=2)

if __name__ == "__main__":
    print(scrape_rss_feed())