# Hämta kontoplanen från Fortnox API och spara som CSV.
#
# Guide: https://jonashertz.com/2026/09/16/fortnox-api-python/
# Kräver: pip install keyring requests pandas
#
# Kör hela filen med: python fortnox_api_python.py
# Eller kopiera varje steg till en egen cell i Jupyter, som i guiden.

import getpass

import keyring
import pandas as pd
import requests

# Steg 1: Spara nycklarna i Windows autentiseringshanterare (bara första gången)
if not keyring.get_password("fortnox", "client-id"):
    keyring.set_password("fortnox", "client-id", getpass.getpass("Client ID: "))
    keyring.set_password("fortnox", "client-secret", getpass.getpass("Client secret: "))
    keyring.set_password("fortnox", "tenant-id", getpass.getpass("Tenant ID: "))
    print("Sparat")

# Steg 2: Hämta en access token
client_id = keyring.get_password("fortnox", "client-id")
client_secret = keyring.get_password("fortnox", "client-secret")
tenant_id = keyring.get_password("fortnox", "tenant-id")

response = requests.post(
    "https://apps.fortnox.se/oauth-v1/token",
    data={"grant_type": "client_credentials"},
    auth=(client_id, client_secret),
    headers={"TenantId": tenant_id},
)
response.raise_for_status()
access_token = response.json()["access_token"]
print("Token hämtad")

# Steg 3: Hämta kontoplanen
response = requests.get(
    "https://api.fortnox.se/3/accounts",
    headers={
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    },
)
response.raise_for_status()

df = pd.json_normalize(response.json()["Accounts"])
print(df.head(20))

# Steg 4: Spara som CSV
df.to_csv("konton.csv", index=False, sep=";", encoding="utf-8-sig")
print("Sparat till konton.csv")
