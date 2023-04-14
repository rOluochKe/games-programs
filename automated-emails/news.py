import requests
from pprint import pprint


class NewsFeed:
    """Representing multiple news titles and links as a single string."""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "227d68bfe4f94ac0b7c5de8e22f2684d"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&' \
              f'apiKey={self.api_key}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
          email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


news_feed = NewsFeed(interest="nasa", from_date="2023-04-01", to_date="2023-04-14", language="en")
pprint(news_feed.get())