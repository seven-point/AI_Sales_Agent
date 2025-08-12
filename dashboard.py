import streamlit as st
import pandas as pd
from crm_utils import init_db, get_pending_leads, update_lead_status
from crm_utils import DB_PATH
import sqlite3
import requests

API_BASE = "http://localhost:8000"  # Change to your deployed FastAPI URL

init_db()

st.set_page_config(page_title="AI Sales Follow-up CRM", layout="wide")
st.title("📞 AI Sales Follow-up CRM")

# View Leads
st.subheader("Lead List")
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM leads", conn)
conn.close()
st.dataframe(df)

# Add Lead
st.subheader("Add New Lead")
with st.form("add_lead"):
    name = st.text_input("Name")
    phone = st.text_input("Phone (with country code)")
    status = "pending"
    submitted = st.form_submit_button("Add Lead")
    if submitted and name and phone:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO leads (name, phone, status) VALUES (?, ?, ?)", (name, phone, status))
        conn.commit()
        conn.close()
        st.success("Lead added successfully!")
        st.experimental_rerun()

# Run Follow-ups
if st.button("🚀 Run AI Follow-ups for Pending Leads"):
    res = requests.post(f"{API_BASE}/run-followups").json()
    st.json(res)
    st.success("Follow-ups completed!")
    st.experimental_rerun()
