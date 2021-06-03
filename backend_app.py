from data_retrieval import get_specific_crypto_info
from coin_manager import supported_coins
from dataframe_maker import export_to_csv
from datetime import datetime
from pprint import pprint
from system_functions import clear_screen
import pandas as pd
from time import sleep


# Iteratively checks prices of all supported coins
# ≈11.3sec runtime @ 17 supported coins
def check_price_all_coins():
    checking_prices = True
    try:
        while checking_prices:
            coin_prices = dict()

            for coin in supported_coins:
                now = datetime.now().strftime('%m/%d/%y @ %H:%M:%S')
                coin_value = get_specific_crypto_info(coin, 'PRICE')
                coin_prices[coin] = [coin_value, now]

            # Put all of the new information in the database
            framework = {
                'Time': [coin_prices[coin][1] for coin in supported_coins],
                'Coins': [coin for coin in coin_prices],
                'USD Values': [coin_prices[coin][0] for coin in supported_coins]
            }

            df = pd.DataFrame(framework, columns=['Time', 'Coins',
                                                  'USD Values'])
            export_to_csv(df, file_name='masterRecord.csv')

            # Display the results
            clear_screen()
            pprint(df)

            # Check every minute
            sleep(60)

    except KeyboardInterrupt:
        print('Keyboard interruption...')
        sleep(0.75)


if __name__ == '__main__':
    check_price_all_coins()
