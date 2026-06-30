import os
import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://xsqsixptymoevzkboove.supabase.co"
SUPABASE_KEY = "sb_publishable_6Ydap-6Y1fvwHmAeFdLlLA_f2co4KSr"

url = st.secrets.get("SUPABASE_URL", None) or os.environ.get("SUPABASE_URL", SUPABASE_URL)
key = st.secrets.get("SUPABASE_KEY", None) or os.environ.get("SUPABASE_KEY", SUPABASE_KEY)

supabase: Client = create_client(url, key)