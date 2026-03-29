from supabase import create_client

SUPABASE_URL = ""
SUPABASE_KEY = "s"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("users").select("*").execute()

records = response.data

print(records)
