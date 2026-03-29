from supabase import create_client

SUPABASE_URL = "https://lhkkhhqkqmtbeeswdjuq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxoa2toaHFrcW10YmVlc3dkanVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNTQxMjksImV4cCI6MjA4ODgzMDEyOX0.XpAwHZiAB-lTh1Hro2XP4VQTKyD0ofow-4jBYfaNrts"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("users").select("*").execute()

records = response.data

print(records)