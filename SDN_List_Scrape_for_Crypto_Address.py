import requests
import pandas as pd
import datetime

'''
563. What is the structure of a digital currency address on OFAC’s SDN List?

Digital currency addresses listed on the SDN List include their unique
alphanumeric identifier (up to 256 characters) and identify the digital
currency to which the address corresponds (e.g., Bitcoin (XBT), Ethereum
(ETH), Litecoin (LTC), Neo (NEO), Dash (DASH), Ripple (XRP), Iota (MIOTA),
Monero (XMR), and Petro (PTR)). Each digital currency address listed on the SDN
list will have its own field: the structure will always begin with “Digital
Currency Address”, followed by a dash and the digital currency’s symbol 
(e.g., “Digital Currency Address - XBT”, “Digital Currency Address - ETH”).
This information is followed by the unique alphanumeric identifier of the
specific address. [06-06-2018]
'''

# Use requests to pull data from SDN List csv hosted online, keep in string var
r = requests.get('https://www.treasury.gov/ofac/downloads/sdn.csv')
string = r.text

# Accumulation list is outside of the function
# and passed into the so that it's not overwritten
address_list = []

def find_coin_address(string, address_list):
    
    # In explaining the structure of digital currency addresses on OFAC SDN List
    # it is said that the structure will always begin with:
    # “Digital Currency Address”
    # Thus, we will use this as our indicator when parsing through the List
    indicator = "Digital Currency Address - "
    
    if indicator in string:
        location = string.find(indicator)
        coin = string[location + len(indicator):].split()[0]
        address = string[location + len(indicator):].split()[1]
        address = address[0:len(address)-1]
        print(coin, address)
        pair = [coin, address]
        address_list.append(pair)
        string = string[location + len(indicator):]
        find_coin_address(string, address_list)
    else:
        print("")
        
# Call the function we wrote above, and create a dataframe with returned data
find_coin_address(string, address_list)
df = pd.DataFrame(address_list, columns=['Coin', 'Address'])

# A list of all the coins talked about on the FAQ (563.) copied at the top
SDN_coins = [
    ["XBT", "Bitcoin"],
    ["ETH", "Ethereum"],
    ["LTC", "Litecoin"],
    ["NEO", "NEO"],
    ["DASH", "DASH"],
    ["XRP", "Ripple"],
    ["MIOTA", "IOTA"],
    ["XMR", "Monero"],
    ["PTR", "Petro"]
]

# Loop through the SDN_coins list above, and print how many of each on SDN List
for coin in SDN_coins:
    if len(df[df['Coin'] == coin[0]]) > 0:
           print(len(df[df['Coin'] == coin[0]]),
                     coin[1], "addresses on the SDN List")

# Get date, and export dataframe as CSV
date = str(datetime.date.today())
csv = 'OFAC_CRYPTO_ADDRESS_CHECK_' + date + '.csv'
df_csv = df.to_csv(csv, index=False)
