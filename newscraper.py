
from newsapi import newsapi_client, NewsApiClient

newsapi = NewsApiClient(api_key='caff3d443ebd44c88803dc48fc10f232')

# /v2/top-headlines
all_articles = newsapi.get_everything(q='medford', sources="google-news")