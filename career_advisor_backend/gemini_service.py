import os
import json
import google.generativeai as genai

# ⚠️ Directly using API key (not safe for production, but works for testing)
API_KEY = "AIzaSyC4MhDSaKEsXGHzewh3cvNWZcazHWD3An0"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_career_advice(user_data):
    required_keys = ['interests', 'skills', 'education', 'career_category']
    if not all(k in user_data for k in required_keys):
        return {"error": "Incomplete user profile"}

    prompt = f"""
    You are a personalized AI career advisor for students in India.
    Based on the following profile and the user's chosen career category,
    provide a detailed and actionable career path recommendation.

    Interests: {user_data['interests']}
    Skills: {user_data['skills']}
    Education: {user_data['education']}
    Career Category: {user_data['career_category']}

    Respond in JSON with:
    {{
      "career_path": "...",
      "milestones": [{{"stage": "...", "duration": "..."}}],
      "required_skills": ["..."],
      "certifications": ["..."],
      "learning_resources": ["..."],
      "market_outlook": "..."
    }}
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            print("[Gemini Warning] Failed to parse JSON. Returning raw response.")
            return {"raw_response": text}

    except Exception as e:
        print(f"[Gemini Error] {e}")
        return None