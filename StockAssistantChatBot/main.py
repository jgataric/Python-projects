import json
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

client = OpenAI(api_key=open('API_KEY', 'r').read())

def get_stock_price(ticker):
    price = yf.Ticker(ticker).history(period='1y').iloc[-1].Close
    return f"The current stock price for {ticker} is ${price:.2f}."

def calculate_SMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.rolling(window=window).mean().iloc[-1])

def calculate_EMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.ewm(span=window, adjust=False).mean().iloc[-1])

def calculate_RSI(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    delta = data.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=14-1, adjust=False).mean()
    ema_down = down.ewm(com=14-1, adjust=False).mean()
    rs = ema_up / ema_down
    return str(100 - (100 / (1 + rs)).iloc[-1])

def calculate_MACD(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    short_EMA = data.ewm(span=12, adjust=False).mean()
    long_EMA = data.ewm(span=26, adjust=False).mean()

    MACD = short_EMA - long_EMA
    signal = MACD.ewm(span=9, adjust=False).mean()
    MACD_histogram = MACD - signal

    return f'{MACD[-1]}, {signal[-1]}, {MACD_histogram[-1]}'

def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y')
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.Close)
    plt.title(f'{ticker} Stock price over last year')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.grid(True)
    plt.savefig('stock.png')
    plt.close()

functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_SMA',
        'description': 'Calculate the simple moving average for a given stock ticker and a window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA.'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_EMA',
        'description': 'Calculate the exponential moving average for a given stock ticker and a window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the EMA.'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    {
        'name': 'calculate_RSI',
        'description': 'Calculate the RSI for a given stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_MACD',
        'description': 'Calculate the MACD for a given stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'plot_stock_price',
        'description': 'Plot the stock price for the last year given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., TSLA for Tesla, Inc.).'
                }
            },
            'required': ['ticker']
        }
    }
]

available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'calculate_RSI': calculate_RSI,
    'calculate_MACD': calculate_MACD,
    'plot_stock_price': plot_stock_price
}

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('Stock Chatbot')

user_input = st.text_input('Your input: ')
if user_input:
    try:
        st.session_state['messages'].append({'role': 'user', 'content': f'{user_input}'})

        response = client.chat.completions.create(
            model='gpt-4o',
            messages=st.session_state['messages'],
            functions=functions,
            function_call='auto'
        )

        response_message = response.choices[0].message

        if response_message.function_call:
            function_name = response_message.function_call.name
            function_args = json.loads(response_message.function_call.arguments)

            if function_name in available_functions:
                function_to_call = available_functions[function_name]
                function_response = function_to_call(**function_args)

                st.text(function_response)

                st.session_state['messages'].append({
                    'role': 'assistant',
                    'content': function_response
                })

            else:
                st.error(f"Function '{function_name}' not found in available functions.")


        else:
            st.text(response_message.content)
            st.session_state['messages'].append({'role': 'assistant', 'content': response_message.content})

    except Exception as e:
        st.error(f"Error: {str(e)}")
