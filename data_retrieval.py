import cryptocompare
from datetime import datetime
import pandas as pd

"""
CryptoCompare API Data Points to note:
MEDIAN          -       Average price over 24hrs
CHANGEPCTDAY    -       % change over 24hrs
PRICE           -       Current price
"""


def get_current_time():
    moment_in_time = datetime.now()

    # Date Format:  MM/DD/YY
    # Time Format: HH:MM:SS
    date_today = moment_in_time.strftime('%m/%d/%Y')
    time_now = moment_in_time.strftime('%H:%M:%S')

    return date_today, time_now


def get_specific_crypto_info(coin, data_point):
    currency = 'USD'
    specific_value = cryptocompare.get_price(coin=coin,
                                             currency=currency,
                                             full=True)['RAW'][coin][currency][data_point]
    return specific_value


def get_all_crypto_info(coin):
    currency = 'USD'
    all_data = cryptocompare.get_price(coin=coin,
                                       currency=currency,
                                       full=True)['RAW'][coin][currency]
    return all_data


# Takes current {username}Coins.csv file and converts to usable Python dictionary
def get_dictionary_from_portfolio_csv(username):
    df = pd.read_csv(f'{username}Coins.csv')
    coins = list()
    amounts = list()
    usd_amounts = list()
    colours = list()
    line_styles = list()

    for i in range(len(df)):
        coins.append(df['Coin'][i])
        amounts.append(df['Amount'][i])
        usd_amounts.append(df['USD Amount'][i])
        colours.append(df['Colour'][i])
        line_styles.append(df['Linestyle'][i])

    framework = {
        'Coin': coins,
        'Amount': amounts,
        'USD Amount': usd_amounts,
        'Colour': colours,
        'Linestyle': line_styles
    }

    return framework


if __name__ == '__main__':
    pass
