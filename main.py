import argparse
import time
from bs4 import BeautifulSoup
import requests

def monitor_keywords(keywords, frequency):
    print("Starting keyword monitor...")
    while True:
        print(f"Monitoring for keywords: {keywords}")
        for keyword in keywords:
            search_url = f"https://news.google.com/search?q={keyword}"
            response = requests.get(search_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('article')
                print(f"Keyword: {keyword}")
                for i, result in enumerate(results[:5]):
                    title = result.find('h3').text if result.find('h3') else "No Title"
                    link = result.find('a')['href'] if result.find('a') else "No Link"
                    print(f"  Article {i + 1}: {title} \n    Link: {link}")
            else:
                print(f"Failed to fetch results for keyword: {keyword}")
        print(f"Sleeping for {frequency} seconds...")
        time.sleep(frequency)

def main():
    parser = argparse.ArgumentParser(description="Monitor and track keyword mentions online.")
    parser.add_argument('--keywords', type=str, required=True, help="Comma-separated keywords to track.")
    parser.add_argument('--frequency', type=int, default=60, help="Check frequency in seconds. Default is 60.")
    
    args = parser.parse_args()

    # Fix: Ensure keywords argument is not empty after splitting
    if not args.keywords.strip():
        print("Error: --keywords argument cannot be empty.")
        return

    keywords = [kw.strip() for kw in args.keywords.split(',') if kw.strip()]

    if not keywords:
        print("Error: No valid keywords provided after parsing.")
        return

    frequency = args.frequency
    monitor_keywords(keywords, frequency)

if __name__ == "__main__":
    main()