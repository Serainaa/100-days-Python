import requests
import os
from twilio.rest import Client

# Constants and API keys
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_stock_key = ""  # Add your API key
api_news_key = ""  # Add your API key
stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"
AUTH_TOKEN = ""  # Add your Twilio authentication token
ACCOUNT_SID = ""  # Add your Twilio account SID

# Parameters for stock API request
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": api_stock_key,
}

news_parameters = {
    "apiKey": api_news_key,
    "qInTitle": COMPANY_NAME,
}

# Fetching stock data
response = requests.get(url=stock_url, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
last_one = float(data_list[0]['4. close'])
previous_one = float(data_list[1]['4. close'])

# Calculating stock percentage change
percentage = (previous_one - last_one) / float(previous_one) * 100
up_down = None
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Checking for significant changes and fetching news
if abs(percentage) > 0.2:
    second_response = requests.get(url=news_url, params=news_parameters)
    second_response.raise_for_status()
    articles = second_response.json()
    three_articles = articles["articles"][:3]
    message = [f"Headline: {article['title']}, Brief: {article['description']}" for article in three_articles]
    print(message)

    # Sending news via Twilio SMS
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for i in range(3):
        message_is = f"{percentage}% {up_down} {message[i]}"
        message_send = client.messages.create(body=message_is, from_='+15075165802', to='+306943929066')

    print(message_send.sid)
else:
    print("Everything is okay")
