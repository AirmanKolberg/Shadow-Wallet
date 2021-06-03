from data_retrieval import *
from os import path
from matplotlib import pyplot as plt
from dataframe_maker import new_user_csv_questions, create_new_csv


# Retrieves a dictionary containing the portfolio values
def get_current_portfolio_values(framework):
    coins = list()

    # Calculate USD values for each coin and add to the array
    for coin in framework:
        coin_name = framework[coin]

        coins.append(coin_name)

    # Get coin values
    new_coins = coins[0]
    amounts = coins[1]
    usd_amounts = coins[2]
    colours = coins[3]
    line_styles = coins[4]

    new_usd_amounts = list()

    for coin in coins:
        if coin != 'Total':
            usd_price = get_specific_crypto_info(coin, 'PRICE')
            new_usd_amounts.append(usd_price)

    for i in range(len(coins) - 1):
        amount = (amounts[i] * new_usd_amounts[i]).__round__(2)
        input(amount)

    """

    # Format the dictionary variable
    # It should look like the following example:

    portfolio_values = {
        'ADA': [4327.46328, 6830.25, 'dashdot', 'blue'],
        'BTC': [2.02528, 80278.62, 'solid', 'gold'],
        'ETH': [0.792502, 2198.33, '-.', 'green'],
        'Total': ['', 88307.2, 'dashed', 'black'],
    }

    """

    portfolio_values = dict()
    for i in range(len(coins)):
        portfolio_values[new_coins[i]] = [amounts[i], usd_amounts[i],
                                          colours[i], line_styles[i]]

    return portfolio_values


def update_portfolio_csv(framework):
    coins = list()
    amounts = list()
    usd_amounts = list()
    colours = list()
    line_styles = list()

    # Get the current value of the coins
    for i in range(len(framework)):
        coin_name = framework['Coin'][i]
        coin_amount = framework['Amount'][i]
        colour = framework['Colour'][i]
        line_style = framework['Linestyle'][i]

        coins.append(coin_name)
        amounts.append(coin_amount)
        colours.append(colour)
        line_styles.append(line_style)


# Needs some work
"""

    for coin in framework['Coin']:
        if coin != '':
            usd_price = get_specific_crypto_info(coin, 'PRICE')

            # Put variables in their respective arrays
            usd_amounts.append(usd_price)
            coins.append(coin)

        # Get our current asset's value
        asset_value = (usd_price * current_coins[coin]).__round__(2)

        # Add the current asset's value to the running total
        total_value += asset_value

        # Save the coins with the comma separating large numbers (ie 1,000)
        if coin == 'ETH':
            eth_value = [f'{asset_value:,}']
        elif coin == 'XRP':
            xrp_value = [f'{asset_value:,}']
        elif coin == 'BTC':
            btc_value = [f'{asset_value:,}']
        elif coin == 'XTZ':
            xtz_value = [f'{asset_value:,}']
        elif coin == 'ADA':
            ada_value = [f'{asset_value:,}']

    # Round the total to the nearest penny
    total_value = total_value.__round__(2)
    print(f'Your crypto portfolio is currently valued at:  ${total_value}')

    the_date, the_time = get_current_time()

    framework = {
        'Date': [the_date],
        'Time': [the_time],
        'ETH Value': eth_value,
        'XRP Value': xrp_value,
        'BTC Value': btc_value,
        'XTZ Value': xtz_value,
        'ADA Value': ada_value,
        'Portfolio Value': [f'{total_value:,}']
    }

    df = pd.DataFrame(framework, columns=['Date', 'Time', 'ETH Value', 'XRP Value',
                                          'BTC Value', 'XTZ Value', 'ADA Value',
                                          'Portfolio Value'])

    if path.exists('runningPortfolio.csv'):
        df.to_csv('runningPortfolio.csv', mode='a', header=False)
    else:
        df.to_csv('runningPortfolio.csv')
"""

# Also needs work...
"""
def plot_data():
    df = pd.read_csv('runningPortfolio.csv')

    # Create a dictionary from the user's coins
    coin_array = list()
    # Give each coin a different colour/line type
    for coin in coin_dict:
        plt.plot(date, coin_dict[coin][0], color=coin_dict[coin][1],
                 linestyle=coin_dict[coin][2])
        for i in range(0, len(df)):
            the_coin = coin_dict[coin][0]
            plt.text(date[i], the_coin[i], f'{the_coin[i]}')

    # Create the key on the right side
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
               fancybox=True, shadow=True)

    # Display the graph on the screen
    plt.show()
"""


if __name__ == '__main__':
    # framework = get_dictionary_from_portfolio_csv('tj')
    # values = get_current_portfolio_values(framework)

    dictionary_array = new_user_csv_questions()
    create_new_csv('tj', dictionary_array)
