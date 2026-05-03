import pytest
from core.monitor import KeywordMonitor

class MockMonitor(KeywordMonitor):
    def fetch_articles(self, keyword):
        if keyword == "test_error":
            return None
        return "<html><body><article><h3>Test Article</h3><a href=\"https://example.com\">Read more</a></article></body></html>"

def test_fetch_articles():
    monitor = MockMonitor(["test"], 5)
    html = monitor.fetch_articles("test")
    assert html is not None

def test_parse_articles():
    monitor = MockMonitor(["test"], 5)
    html = "<html><body><article><h3>Sample Title</h3><a href=\"sample_link\">Link</a></article></body></html>"
    articles = monitor.parse_articles(html)
    assert len(articles) == 1
    assert articles[0]["title"] == "Sample Title"
    assert articles[0]["link"] == "sample_link"

def test_no_articles():
    monitor = MockMonitor(["test"], 5)
    html = "<html><body></body></html>"
    articles = monitor.parse_articles(html)
    assert len(articles) == 0