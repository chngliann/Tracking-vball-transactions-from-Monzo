from pandas.io.json import json_normalize
import pandas as pd
from monzo import Monzo
from monzo import MonzoOAuth2Client

# Authenticate
oauth_client = MonzoOAuth2Client.from_json(r'C:\Users\chngl\OneDrive\Documents\GitHub\Tracking-vball-transactions-from-Monzo\monzo.json')
client = Monzo.from_oauth_session(oauth_client)

# Request transactions
account_id = client.get_first_account()['id']
transactions = client.get_transactions(account_id)

# Flatten json data and save
tr_table = json_normalize(transactions['transactions'])
tr_table = pd.DataFrame(tr_table, sort = False)
tr_table.to_csv(r'C:\Users\chngl\OneDrive\Documents\GitHub\Tracking-vball-transactions-from-Monzo\Monzo_transactions.csv', sep=',', index = False)