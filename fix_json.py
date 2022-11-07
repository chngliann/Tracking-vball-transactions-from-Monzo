import json
from monzo.utils import load_token_from_file

jsonfile = load_token_from_file(r'C:\Users\chngl\OneDrive\Documents\GitHub\Tracking-vball-transactions-from-Monzo\monzo.json')
jsonfile['client_secret'] = 'mnzconf.F5FFrssMFVq+kOxtYyKzOVZn4A6hRK7NrVuCRaPw1J84626NYZA9q326G8GM0msl0AlUV3oN4XQOUZXT4VnhYw=='
with open(r'C:\Users\chngl\OneDrive\Documents\GitHub\Tracking-vball-transactions-from-Monzo\monzo.json', 'w') as js:
    json.dump(jsonfile, js)