import requests
import json
'''
Using bitFlyer's chainFlyer API to access bitcoin address and transaction hash information
Using requests library to access the chainFlyer API
Using json to quickly and easily reformat the incoming API information
Built classes that allow for accessing specific pieces of info about addresses and TX hashes
'''
class Address:

    def __init__(self, address):
        # a = bitcoin_explorer.Address('xbt')
        # ADDRESS a.address
        self.address = str(address)

        url = 'https://chainflyer.bitflyer.com/v1/address/' + str(address)
        r = requests.get(url)
        j = r.json()

        # ADDRESS BALANCE a.balance
        self.balance = j['confirmed_balance'] * .00000001
        # PENDING DEPOSITS a.pending
        self.pending = (j['unconfirmed_balance'] - j['confirmed_balance']) * .00000001

class Hash:

    def __init__(self, tx):
        # tx = bitcoin_explorer.Hash('000000')
        # TX HASH tx.tx
        self.tx = str(tx)

        url = 'https://chainflyer.bitflyer.com/v1/tx/' + str(tx)
        r = requests.get(url)
        j = r.json()
        
        # WHICH BLOCK? tx.block
        self.block = str(j['block_height'])
        # HOW MANY CONFIRMATIONS? tx.confirmations
        self.confirmations = int(j['confirmed'])
        # WHAT FEES WERE PAID? tx.fees
        self.fees = int(j['fees']) * .00000001
        # BYTE SIZE tx.byte_size
        self.byte_size = int(j['size'])
        
        date = str(j['received_date']).split('T')
        # DATE OF TX tx.date
        self.date = date[0]
        # DATE AND TIME OF TX tx.datetime
        self.datetime = date[0] + ' ' + date[1]
        
        prev_hash = []
        input_add = []
        for item in j['inputs']:
            inputs = str(item).split()
            prev_hash.append(str(inputs[1]).rstrip().strip("','"))
            input_add.append(str(inputs[9]).rstrip().strip("','"))
        # PREVIOUS TX HASH tx.last_tx
        self.last_tx = prev_hash
        # INPUT ADDRESS tx.input
        self.input = input_add

        output_add = []
        for item in j['outputs']:
            outputs = str(item).split()
            output_add.append(str(outputs[5]).rstrip().strip("',}]'"))
        # OUTPUT ADDRESS tx.output
        self.output = output_add
        

        
