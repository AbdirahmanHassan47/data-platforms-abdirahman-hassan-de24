import time

# from connect_crypto_api import Cryptocurrency
from quixstreams import Application
from constanst import COINMARKET_API

from requests import Session
import json
from pprint import pprint

app = Application(
    broker_address="localhost:9092",
    consumer_group="coin_group",
)

coins_topic = app.topic(name="coins", value_serializer="json")

api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
def get_latest_coin_data(symbol="BTC"):

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COINMARKET_API,
    }

    parameters = {
        "symbol": symbol,
        "convert": "USD",
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(api_url, params=parameters)

    #print("API Response:", response.status_code, response.text)
    return json.loads(response.text)["data"][symbol]


def main():

    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_coin_data("BTC")

            kafka_message = coins_topic.serialize(
                key=coin_latest["symbol"], value=coin_latest
            )

            print(
                f"produce event with key = {kafka_message.key}, price = {coin_latest['quote']['USD']['price']}"
            )
            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )

            time.sleep(30)


if __name__ == "__main__":
    main()
    #pprint(get_latest_coin_data("BTC")["quote"])