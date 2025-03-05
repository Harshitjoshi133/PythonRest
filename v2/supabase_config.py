import os
from dotenv import load_dotenv
from supabase import create_client, Client
load_dotenv()
# Load Supabase credentials from environment variables
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

if not supabase_url or not supabase_key:
    raise Exception("SUPABASE_URL or SUPABASE_KEY environment variable not set")

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)