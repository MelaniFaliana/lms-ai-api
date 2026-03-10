from fastapi import FastAPI
import google.generativeai as genai
import json
import re

app = FastAPI()

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.post("/generate-question")
def generate_question(materi: str):

    prompt = f"""
    Berdasarkan materi berikut:

    {materi}

    Buatkan 5 soal pilihan ganda.

    Format JSON:

    {{
      "questions":[
        {{
          "question":"...",
          "options":{{"A":"","B":"","C":"","D":""}},
          "answer":"A"
        }}
      ]
    }}
    """

    response = model.generate_content(prompt)

    text = response.text

    json_text = re.search(r'\{.*\}', text, re.DOTALL).group()

    data = json.loads(json_text)


    return data
