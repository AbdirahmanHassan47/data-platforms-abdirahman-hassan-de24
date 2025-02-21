# connect_api.py
import requests
import json
 
def fetch_crypto_data(api_key, endpoint="v1/cryptocurrency/listings/latest"):
    url = f"https://pro-api.coinmarketcap.com/{endpoint}"
    headers = {"X-CMC_PRO_API_KEY": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
 
# coin_producer.py
import time
from connect_api import fetch_crypto_data
 
def producer_loop(api_key, interval=60):
    while True:
        data = fetch_crypto_data(api_key)
        if data:
            with open("crypto_data.json", "w") as f:
                json.dump(data, f)
        time.sleep(interval)
 
# dashboard.py
import pandas as pd
import streamlit as st
import json
 
def load_data():
    with open("crypto_data.json", "r") as f:
        data = json.load(f)
    return data
 
def visualize_data():
    data = load_data()
    df = pd.DataFrame(data["data"])  # Anpassa efter API-svar
    st.title("Kryptokollen Dashboard")
    selected_currency = st.selectbox("Välj kryptovaluta", df["symbol"].unique())
    filtered_df = df[df["symbol"] == selected_currency]
    st.line_chart(filtered_df[["quote"]]["USD"]["price"]])
    st.write(filtered_df)
 
if __name__ == "__main__":
    visualize_data()
 
# requirements.txt
requests
pandas
streamlit