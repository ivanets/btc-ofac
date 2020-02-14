import SDN_List_Scrape_Crypto_Address
''' 
Once this .py file is imported, its code is executed, and it's the source of our imported data read into variable 'df'
'''
import pandas as pd
import datetime
import requests
from bitcoin_explorer import Address

date = str(datetime.date.today())
csv = 'OFAC_CRYPTO_ADDRESS_CHECK_' + date + '.csv'

df = pd.read_csv(csv)
OFAC_coin_balances = []
# Only able to check XBT or Bitcoin address balances on the SDN List with the bitcoin_explorer script
df_btc = df[df['Coin'] == 'XBT']

for item in df_btc['Address']:
    a = Address(item)
    OFAC_coin_balances.append([a.address, a.balance, a.pending])

df_ofac = pd.DataFrame(OFAC_coin_balances,
                       columns=['Address', 'Balance', 'Unconfirmed Coin'])

# Export csv with BTC addresses on OFAC with balances and pending coins
csv_BTC_OFAC = 'OFAC_BTC_ADDRESS_WITH_BALANCE' + date + '.csv'
export_csv = df_ofac.to_csv(csv_BTC_OFAC, index=False)

