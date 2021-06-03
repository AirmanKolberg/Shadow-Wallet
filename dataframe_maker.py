import pandas as pd
from os import path
from coin_manager import supported_coins, verify_yes_or_no, get_float_value_from_user
from data_retrieval import get_specific_crypto_info


def export_to_csv(df, file_name):
    if path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False)
    else:
        df.to_csv(file_name)


"""
Add a new coin to your portfolio!
This takes in the new coin, as well
as the number of coins that user holds
stored as a float value.
"""


# Add a new type of coin to the portfolio
def add_new_coin(new_coin, num_of_coins=False):

    # Skips if the coin is already selected
    if not new_coin:
        new_coin = input('Select coin: ').upper()
        if new_coin not in supported_coins:
            print(f"{new_coin} is not (yet) supported, please try again.")
            new_coin, num_of_coins = add_new_coin(new_coin=False)

    # Skips if this value was retrieved during recursion 2 lines up ^^
    if not num_of_coins:
        num_of_coins = get_float_value_from_user('Select number of coins: ')

    return new_coin, num_of_coins


def new_user_csv_questions():

    questions = ["Colour for this coin's line graph: ",
                 """Linestyle for this coin's line graph:
(ie '-.', ':', 'solid', 'dotted', 'dashdot', 'dashed', etc.)
"""]
    coins = list()
    coins_to_add = True

    while coins_to_add:

        coins_to_add = verify_yes_or_no(input('Add a new coin to your portfolio?\n'))

        # Determine if more coins are to be added
        if not coins_to_add:

            return coins

        # Add a new coin/coin amount to portfolio
        new_coin, num_of_coins = add_new_coin(new_coin=False)
        answers = list()

        for question in questions:
            response = input(question)
            answers.append(response)

        usd_value = (num_of_coins * get_specific_crypto_info(new_coin, 'PRICE')).__round__(2)

        framework = {
            new_coin: [num_of_coins, usd_value, answers[0], answers[1]]
        }
        coins.append(framework)


def create_new_csv(username, dictionary_array):

    # Declare arrays needed for pd.DataFrame
    coins = list()
    amounts = list()
    usd_amounts = list()
    colours = list()
    line_styles = list()

    # Put the data from the dictionary into their arrays
    for coin in dictionary_array:
        for key in coin:
            coins.append(key)
            amounts.append(coin[key][0])
            usd_amounts.append(coin[key][1])
            colours.append(coin[key][2])
            line_styles.append(coin[key][3])

    # Get the last info for the "Total" column
    last_colour = input("Choose colour for 'Total' line on graph: ")
    last_line_style = input("Finally, Total's linestyle: ")

    # Append the "Total" information
    coins.append('Total')
    amounts.append('')
    usd_amounts.append(sum(usd_amounts).__round__(2))
    colours.append(last_colour)
    line_styles.append(last_line_style)

    framework = {
        'Coin': coins,
        'Amount': amounts,
        'USD Amount': usd_amounts,
        'Colour': colours,
        'Linestyle': line_styles
    }

    df = pd.DataFrame(framework, columns=['Coin', 'Amount', 'USD Amount',
                                          'Colour', 'Linestyle'])

    export_to_csv(df, f'{username}Coins.csv')


if __name__ == '__main__':
    pass
