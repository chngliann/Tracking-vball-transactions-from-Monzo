from monzo import MonzoOAuth2Client # Import OAuth client class

oauth_client = MonzoOAuth2Client('oauth2client_0000APELfVhlgvhA7qz8xV', 'mnzconf.F5FFrssMFVq+kOxtYyKzOVZn4A6hRK7NrVuCRaPw1J84626NYZA9q326G8GM0msl0AlUV3oN4XQOUZXT4VnhYw==',redirect_uri='https://localhost') # Replace with details entered on developer playground.

auth_start_url = oauth_client.authorize_token_url() # Returns a dictionary containing the Monzo authentication startpoint.

print(auth_start_url)

oauth_client.fetch_access_token('eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6IklFcHBjLytQT2J0b1Z0em92SnQzIiwianRpIjoiYXV0aHpjb2RlXzAwMDBBUEVNRkVHTzE0dUdTTUQzSVkiLCJ0eXAiOiJhemMiLCJ2IjoiNiJ9.v1HY20ZxAEYBYX9x66THyA4IEhay3lViDTKA9mu_ZNIZdXo1f29b9WEiLYVdwbJzVLtc_b2_AKlkLF9Y8m5XFg')



