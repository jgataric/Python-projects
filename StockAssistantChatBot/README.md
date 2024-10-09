Stock Analysis Chatbot
This project is a Streamlit-based chatbot that integrates with OpenAI's GPT model to analyze stock data using various financial metrics and technical indicators like SMA, EMA, RSI, and MACD. The chatbot can return stock prices, plot historical stock data, and respond to user queries regarding stock information.

Features
Retrieve Stock Price: Get the latest stock price for a given ticker symbol.
Simple Moving Average (SMA): Calculate the SMA for a specified window.
Exponential Moving Average (EMA): Calculate the EMA for a given window.
Relative Strength Index (RSI): Calculate the RSI of a stock.
Moving Average Convergence Divergence (MACD): Calculate the MACD for a stock.
Plot Stock Price: Plot the stock price for the last year.
GPT model: Can answer any question because of OpenAI GPT model.

How to Run
Clone the repository and navigate to the project folder.
Create an OpenAI API key and save it in a file called API_KEY (or update the api_key variable in the script).
Run the Streamlit app using the following command:
open terminal and type in following:
streamlit run main.py
The chatbot interface will open in your browser. Type your queries (e.g., stock ticker or specific requests like "Calculate SMA for TSLA") and the chatbot will respond.

Functions Available
get_stock_price(ticker): Returns the latest stock price for the specified ticker symbol.
calculate_SMA(ticker, window): Calculates the Simple Moving Average for a stock over a given window.
calculate_EMA(ticker, window): Calculates the Exponential Moving Average for a stock.
calculate_RSI(ticker): Calculates the Relative Strength Index of the stock.
calculate_MACD(ticker): Calculates the Moving Average Convergence Divergence of the stock.
plot_stock_price(ticker): Plots the stock price over the last year.

How It Works
User Input: The user inputs a query or stock symbol into the text field.
OpenAI Integration: The chatbot uses the OpenAI GPT model to process user queries.
Function Call: Based on the input, the chatbot will call the appropriate function to retrieve or calculate stock data. If the appropriate function is not called, chatbot can answer any question via OpenAI GPT model.
Display: The result (e.g., stock price or indicator) is displayed in the Streamlit interface. If the query is for a plot, the graph will be shown.