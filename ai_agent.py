from huggingface_hub import InferenceApi

# Free Hugging Face model for short text generation
inference = InferenceApi(repo_id="microsoft/DialoGPT-small")

def generate_followup_message(name):
    prompt = f"Generate a polite sales follow-up message for {name} to check their interest in our product."
    response = inference(prompt)
    return response[0]["generated_text"] if isinstance(response, list) else "Hello, just checking in about our offer!"
