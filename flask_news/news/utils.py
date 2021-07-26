from flask import current_app
import requests
import os



def get_news(query, language, category, country, sort_by):
    OWM_Endpoint = "https://newsapi.org/v2/top-headlines?"
    api_key=os.environ.get("api_key") or current_app.config['API_KEY']
    params = {
        'q':query,
        # 'sources':'bbc-news,the-verge',
        'domains':'bbc.co.uk,techcrunch.com',
        'language':language,
        'country': country,
        'category': category,
        'sort_by':sort_by,
        'page':1
        }
    headers = {'X-Api-Key': api_key}

    response = requests.get(url=OWM_Endpoint, params=params, headers=headers)
    result = response.json()
    return result