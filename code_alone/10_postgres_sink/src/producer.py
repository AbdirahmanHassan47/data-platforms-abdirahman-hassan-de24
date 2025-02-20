from quixstreams import Application
from constant import COINMARKET_API
from requests import Session
import json
from pprint import pprint
import time


def get_latest_data(target_symbol = "BTC"):
    API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    parameters = {
    'symbol':target_symbol,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)


    response = session.get(API_URL, params=parameters)
    return json.loads(response.text)
    



#def main():
    app = Application(broker_adress = "localhost:9092", consumer_group="coin_group")
    coins_topic = app.topic(name = "coins", value_serializer="json")


def main():
    app = Application(broker_address = "localhost:9092", consumer_group="coin_group")
    coins_topic = app.topic(name = "coins", value_serializer="json")

    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_data("BTC")
            # pprint(latest_quotes)
            # coin_latest = latest_quotes["quote"]

            kafka_message = coins_topic.serialize(
                key=coin_latest["symbol"], value=coin_latest
            )

            print(
                f"produce event with key = {kafka_message.key}, value = {coin_latest['quote']['USD']['price']}"
            )
            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )

            time.sleep(10)


if __name__ == '__main__':
    main()
    #coina_data = get_latest_data("BTC","qoute")
    #print(coina_data)
