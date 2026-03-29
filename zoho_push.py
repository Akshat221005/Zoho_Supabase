import requests
from supabase import create_client

# SUPABASE CONFIG
SUPABASE_URL = "https://lhkkhhqkqmtbeeswdjuq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxoa2toaHFrcW10YmVlc3dkanVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNTQxMjksImV4cCI6MjA4ODgzMDEyOX0.XpAwHZiAB-lTh1Hro2XP4VQTKyD0ofow-4jBYfaNrts"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ZOHO TOKEN
access_token = "1000.408d9b5b132cad07666bc2c934db5a7a.9665a8bd09e69aed71887a7f28faeafd"

headers = {
    "Authorization": f"Zoho-oauthtoken {access_token}"
}

# Fetch data from Supabase
response = supabase.table("users").select("*").execute()

records = response.data

# Push each record to Zoho CRM
for record in records:

    payload = {
        "data": [
            {
                "First_Name": record["name"],
                "Last_Name": record["last_name"],
                "Email": record["email"],
                "Company": record["company"]
            }
        ]
    }

    zoho_response = requests.post(
        "https://www.zohoapis.in/crm/v2/Leads",
        headers=headers,
        json=payload
    )

    print(zoho_response.json())