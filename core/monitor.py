import time
import requests
from bs4 import BeautifulSoup
import logging

class KeywordMonitor:
    def __init__(self, keywords, frequency):
        self.keywords = keywords
        self.frequency = frequency
        self.base_url = "https://news.google.com/search?q="
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("monitor.log"),
                logging.StreamHandler()
            ]
        )

    def fetch_articles(self, keyword):
        url = f"{self.base_url}{keyword}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching articles for keyword '{keyword}': {e}")
            return None

    def parse_articles(self, html):
        try:
            soup = BeautifulSoup(html, "html.parser")
            articles = []
            for item in soup.select("article"):
                title = item.select_one("h3").text if item.select_one("h3") else "No title"
                link = item.select_one("a")["href"] if item.select_one("a") else "No link"
                articles.append({"title": title, "link": link})
            return articles
        except Exception as e:
            logging.error(f"Error parsing articles: {e}")
            return []

    def monitor_keywords(self):
        while True:
            for keyword in self.keywords:
                html = self.fetch_articles(keyword)
                if html:
                    articles = self.parse_articles(html)
                    logging.info(f"{len(articles)} articles found for '{keyword}': {articles}")
            time.sleep(self.frequency)

    def start(self):
        try:
            self.monitor_keywords()
        except KeyboardInterrupt:
            logging.info("Shutting down keyword monitor.")