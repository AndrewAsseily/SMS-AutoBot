# SMS-AutoBot

SMS-AutoBot is a bot that sends you a message every morning with the weather in New York City, the number of days until your 50th birthday, and the stock price of Paypal. This bot is built using Python and the Twilio API.

## Installation

To install SMS-AutoBot, you'll need to have Python 3 and the Twilio library installed. You can install the Twilio library by running the following command in your terminal:

pip install twilio

Next, clone this repository to your local machine by running the following command:

git clone https://github.com/your-username/SMS-AutoBot.git

## Usage

To use SMS-AutoBot, you'll need to set up a Twilio account and obtain your account SID, auth token, and Twilio phone number. Once you have those, create a file called `secrets.py` in the root directory of the project and add the following lines:

```python
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
twilio_phone_number = 'your_twilio_phone_number_here'
your_phone_number = 'your_phone_number_here'
```
Replace the placeholders with your actual values.

Next, you can run the bot by running the following command:

python3 twilioMorning.py

This will send you a message with the weather in New York City, the number of days until your 50th birthday, and the stock price of Paypal.

