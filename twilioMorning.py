import yfinance as yf
from twilio.rest import Client
import datetime
import requests
import schedule
import time

from keys import weather_api_key, account_sid, auth_token, my_phone_num, sender

client = Client(account_sid, auth_token)

def paypal_stock_price():
    stock_info = yf.Ticker("PYPL").info
    paypal_market_price = stock_info["regularMarketPrice"]
    return paypal_market_price


def get_temperature(location="New York City"):
    api_weather_req = requests.get(
        "http://api.weatherstack.com/current?access_key="
        + weather_api_key
        + "&query="
        + "New York City"
    )
    api_weather_req = api_weather_req.json()
    temperature = api_weather_req["current"]["temperature"]

    return temperature


def days_until_50th_birthday():
    today = datetime.date.today()
    birthday = datetime.date(2051, 10, 9)
    delta = birthday - today
    delta = (str(delta).split(","))[0]
    return delta


def morning_message():
    good_morning = "Good Morning Andrew, "

    temperature = get_temperature("New York City")
    temperature_statement = (
        "The temperature right now is "
        + str(temperature)
        + "°C"
        + " in New York City. "
    )

    birthdays = days_until_50th_birthday()
    birthday_statement = "There are " + str(birthdays) + " until your 50th birthday."

    paypal_price = paypal_stock_price()
    paypal_stock_statement = "The PayPal stock price is $" + str(paypal_price) + "."

    result = (
        good_morning
        + "\n\n"
        + temperature_statement
        + "\n"
        + birthday_statement
        + "\n"
        + paypal_stock_statement
    )

    return result


def message():
    message = client.messages.create(
        to=my_phone_num,  # Andrew
        from_=sender,
        body=morning_message(),
    )


def main():
    #schedule.every().day.at("11:11:00").do(message)
    message()
    


main()


# RUN WITH nohup to keep processes running even after exiting the shell or terminal.
# while True:
#     schedule.run_pending()
#     time.sleep(1)
