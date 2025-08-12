from fastapi import FastAPI
from crm_utils import init_db, get_pending_leads, update_lead_status
from ai_agent import generate_followup_message
from twilio_handler import send_whatsapp_message

app = FastAPI()
init_db()

@app.get("/")
def home():
    return {"message": "AI Sales Follow-up Agent Running"}

@app.post("/run-followups")
def run_followups():
    leads = get_pending_leads()
    results = []
    for lead in leads:
        lead_id, name, phone = lead
        message = generate_followup_message(name)
        send_whatsapp_message(phone, message)
        update_lead_status(lead_id, "contacted")
        results.append({"lead": name, "status": "contacted"})
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)