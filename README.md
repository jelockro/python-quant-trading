# QuantTrading
## A machine-learning python implementation of quantitative trading models
This app implements Flask for its server, sqlite3 for its database, and uses webpack and react.


In order to Run, change directories to QuantTrading:
```
cd QuantTrading
```
and enter the following code:

```
npm i 
pipenv install
export FLASK_APP=__init__.py
export FLASK_ENV=development
```
now you can start the app by running:
```
flask run
```

## Stage 1: 
### Web-based Interface to Scrape CyrpotoCurrency Exchange Rate Data

This Program will implement a python based script that pulls crypto-currency real-time exchange rates and historical
data through the Alpha Vantage API. [https://www.alphavantage.co/]
It will utilize FLASk to create Web-Based GUI.  It will serve the UI with React.
