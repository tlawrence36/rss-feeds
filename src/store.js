import { atom } from 'nanostores';

export const feedSources = [
    ['ABC', 'US', 'https://abcnews.go.com/abcnews/usheadlines'],
    ['ABC', 'Top Stories', 'https://abcnews.go.com/abcnews/topstories'],
    ['ABC', 'International', 'https://abcnews.go.com/abcnews/internationalheadlines'],
    ['ABC', 'Money', 'https://abcnews.go.com/abcnews/moneyheadlines'],
    ['ABC', 'Health', 'https://abcnews.go.com/abcnews/healthheadlines'],
    ['ABC', 'Sports', 'https://abcnews.go.com/abcnews/sportsheadlines'],
    ['ABC', 'Entertainment', 'https://abcnews.go.com/abcnews/entertainmentheadlines'],
    ['ABC', 'Tech', 'https://abcnews.go.com/abcnews/technologyheadlines'],
    ['ABC', 'Travel', 'https://abcnews.go.com/abcnews/travelheadlines'],

    ['Allsides', '', 'https://www.allsides.com/rss/news'],

    ['CBS', 'US', 'https://www.cbsnews.com/latest/rss/us'],
    // ['CBS', 'Main', 'https://www.cbsnews.com/latest/rss/main'],
    ['CBS', 'Politics', 'https://www.cbsnews.com/latest/rss/politics'],
    ['CBS', 'World', 'https://www.cbsnews.com/latest/rss/world'],
    ['CBS', 'Health', 'https://www.cbsnews.com/latest/rss/health'],
    ['CBS', 'Money', 'https://www.cbsnews.com/latest/rss/moneywatch'],
    ['CBS', 'Science', 'https://www.cbsnews.com/latest/rss/science'],
    ['CBS', 'Tech', 'https://www.cbsnews.com/latest/rss/technology'],
    ['CBS', 'Entertainment', 'https://www.cbsnews.com/latest/rss/entertainment'],
    ['CBS', 'Space', 'https://www.cbsnews.com/latest/rss/space'],

    ['HuffPost', 'US News', 'https://chaski.huffpost.com/us/auto/vertical/us-news'],
    ['HuffPost', 'Health', 'https://chaski.huffpost.com/us/auto/vertical/health'],
    ['HuffPost', 'Arts', 'https://chaski.huffpost.com/us/auto/vertical/arts'],
    ['HuffPost', 'Celebrity', 'https://chaski.huffpost.com/us/auto/vertical/celebrity'],
    ['HuffPost', 'Media', 'https://chaski.huffpost.com/us/auto/vertical/media'],
    ['HuffPost', 'TV', 'https://chaski.huffpost.com/us/auto/vertical/tv'],

    ['Intercept', '', 'https://theintercept.com/feed/?lang=en'],

    ['NBC', 'News', 'https://feeds.nbcnews.com/nbcnews/public/news'],
    ['NBC', 'Pop Culture', 'https://feeds.nbcnews.com/today/public/popculture'],
    ['NBC', 'World', 'https://feeds.nbcnews.com/nbcnews/public/world'],

    ['NPR', 'National', 'https://feeds.npr.org/1003/rss.xml'], // NPR National
    ['NPR', 'World', 'https://feeds.npr.org/1004/rss.xml'], // NPR World
    ['NPR', 'Business', 'https://feeds.npr.org/1006/rss.xml'], // NPR Business
    ['NPR', 'Science', 'https://feeds.npr.org/1007/rss.xml'], // NPR Science
    ['NPR', 'Politics', 'https://feeds.npr.org/1014/rss.xml'], // NPR Politics
    ['NPR', 'Tech', 'https://feeds.npr.org/1019/rss.xml'], // NPR Tech
    ['NPR', 'Environment', 'https://feeds.npr.org/1025/rss.xml'], // NPR Environment
    ['NPR', 'Space', 'https://feeds.npr.org/1026/rss.xml'], // NPR Space
    ['NPR', 'Books', 'https://feeds.npr.org/1032/rss.xml'], // NPR Books
    // 'https://feeds.npr.org/1054/rss.xml', // NPR Gardening
    // 'https://feeds.npr.org/1053/rss.xml', // NPR Food
    ['NPR', 'Europe', 'https://feeds.npr.org/1124/rss.xml'], // NPR Europe
    ['NPR', 'Asia', 'https://feeds.npr.org/1125/rss.xml'], // NPR Asia
    ['NPR', 'Africa', 'https://feeds.npr.org/1126/rss.xml'], // NPR Africa
    ['NPR', 'Americas', 'https://feeds.npr.org/1127/rss.xml'], // NPR Latin America

    // ['Vox', '', 'https://www.vox.com/rss/index.xml'],

    ['Yahoo', '', 'https://www.yahoo.com/news/rss'],
  ]

export const currentFeed = atom(feedSources[0][0]);