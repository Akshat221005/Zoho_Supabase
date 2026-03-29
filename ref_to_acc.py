import requests

url = "https://accounts.zoho.in/oauth/v2/token"

params = {
    "refresh_token": "1000.98175b9d30b6230286ec287df0822a7c.f1d26599f7eb0af2b13207c35596dc12",
    "client_id": "1000.6YV15QSJTUJ7ZSWQTUT5JC96EWJA6Y",
    "client_secret": "95a944dc7391eaf1c7ff427f1a15caf952f089c053",
    "grant_type": "refresh_token"
}

response = requests.post(url, params=params)

access_token = response.json()["access_token"]

print("Access Token:", access_token)