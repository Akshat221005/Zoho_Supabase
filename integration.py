import requests

url = "https://accounts.zoho.in/oauth/v2/token"

params = {
    "grant_type": "authorization_code",
    "client_id": "1000.6YV15QSJTUJ7ZSWQTUT5JC96EWJA6Y",
    "client_secret": "95a944dc7391eaf1c7ff427f1a15caf952f089c053",
    "redirect_uri": "http://localhost",
    "code": "1000.8148af08248d8a54574298d534505ca3.9fdf2e23c8d6912b3eb008f0aa8ee72d"
}

response = requests.post(url, params=params)
print("Status Code:", response.status_code)
print("Response Text:", response.text)