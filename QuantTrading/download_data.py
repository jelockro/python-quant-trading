#  This program will dowload DAILY data from alphavantage
#  OPEN(SYMBOL), OPEN(USD), HIGH(SYMBOL), HIGH(MARKET), LOW(SYMBOL), LOW(MARKET)
#  CLOSE(SYMBOL), CLOSE(MARKET), VOLUME, MARKETCAP(MARKET)
#
# the form of API queries for alphavantage are below.
# symbol=BTC, ETH, etc.
# market=CNY, USD, etc.
# https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo

alpha_V_API_Key = 81W3D9V8RVRGWDQD

def create_url(symbol, market):
	''' T