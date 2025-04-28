import feedparser
import requests
import time

# ﺖﻨﻈﯿﻣﺎﺗ
RSS_FEEDS = [
    'https://en.mehrnews.com/rss',
    'https://www.tasnimnews.com/en/rss',
    'https://en.irna.ir/rss',
    'https://www.tehrantimes.com/rss',
    'https://www.entekhab.ir/fa/rss/allnews'
]
TELEGRAM_TOKEN = '7340694912:AAHqpuj1laecYit86avX7e6o4q7wScn11t8'
TELEGRAM_CHAT_ID = '@automaticNews1999'
CHECK_INTERVAL = 600  # ﺏﺭﺮﺴﯾ ﻩﺭ 10 ﺪﻘﯿﻘﻫ

# ﺬﺨﯾﺮﻫ ﻞﯿﻨﮐ<200c>ﻫﺎﯾ ﺍﺮﺳﺎﻟ<200c>ﺷﺪﻫ ﺏﺭﺎﯾ ﺞﻟﻮﮕﯾﺮﯾ ﺍﺯ ﺍﺮﺳﺎﻟ ﺖﮐﺭﺍﺮﯾ
sent_links = set()

def send_to_telegram(title, link):
    message = f"{title}\n{link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    return response

def fetch_and_send():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if entry.link not in sent_links:
                send_to_telegram(entry.title, entry.link)
                sent_links.add(entry.link)

if __name__ == '__main__':
    while True:
        fetch_and_send()
        time.sleep(CHECK_INTERVAL)

