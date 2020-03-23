import requests
def get_btc(): #курс биткоина к доллару
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(price) + ' usd'

print(get_btc())