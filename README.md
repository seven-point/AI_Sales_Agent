# 📞 AI Sales Follow-up Agent

An **AI-powered sales follow-up assistant** that:
- Retrieves pending leads from a CRM (SQLite database)
- Generates personalized follow-up messages using a Hugging Face AI model
- Sends messages via WhatsApp using Twilio API
- Updates CRM lead status automatically
- Provides a **Streamlit CRM dashboard** to manage leads and trigger follow-ups

---

## 🚀 Features
- **FastAPI Backend** – Handles lead processing and Twilio message sending
- **Streamlit Dashboard** – Manage leads visually
- **AI Message Generation** – Uses Hugging Face free LLM (DialoGPT-small)
- **CRM Integration** – SQLite database for storing leads and status
- **WhatsApp API** – Twilio integration for real messaging
- **Environment Config** – Secure `.env` file for API keys

---

## 📂 Project Structure
ai-sales-followup-agent/
│── app.py # FastAPI backend
│── crm_utils.py # SQLite CRM helper functions
│── ai_agent.py # Hugging Face AI logic
│── twilio_handler.py # Twilio WhatsApp sending functions
│── dashboard.py # Streamlit CRM dashboard
│── config.py # Loads environment variables
│── requirements.txt # Dependencies
│── .env # Environment variables (not committed)
│── crm.db # SQLite database (auto-created)
│── README.md # Project documentation

##  Install Dependencies
pip install -r requirements.txt

## Create .env File
Create a file named .env in the project root:
# Twilio credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_WHATSAPP_NUMBER=+14155238886  # Twilio Sandbox or Verified Number

# Hugging Face API key
HF_API_KEY=your_huggingface_api_key_here  //Only if inference API doesnt work in your system. Load it in config file and then import in ai_agent.py

# FastAPI base URL
API_BASE_URL=http://localhost:8000

# SQLite database name
CRM_DB=crm.db

## Running
Start FastAPI backend:
python app.py

Start Streamlit dashboard:
streamlit run dashboard.py

You’ll now have:

Backend: http://localhost:8000

CRM UI: Opens in browser at http://localhost:8501
