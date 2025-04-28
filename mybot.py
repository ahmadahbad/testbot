import time
import feedparser
import requests

BOT_TOKEN = '7340694912:AAHqpuj1laecYit86avX7e6o4q7wScn11t8'
CHANNEL_ID = '@automaticNews1999'

FEED_URLS = [
    'https://www.isna.ir/rss',   # خبرگزاری ایسنا
    'https://www.mehrnews.com/rss',  # خبرگزاری مهر
    'https://www.irna.ir/rss'    # خبرگزاری ایرنا
]

sent_links = set()

def fetch_and_send():
    for feed_url in FEED_URLS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if entry.link not in sent_links:
                message = f"📰 {entry.title}\n{entry.link}"
                send_to_telegram(message)
                sent_links.add(entry.link)

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': CHANNEL_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_send()
        time.sleep(600)  # هر ۱۰ دقیقه یکبار اخبار جدید رو بفرسته

