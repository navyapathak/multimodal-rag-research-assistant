import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, context):

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer the question using only the provided context.
    """

    response = model.generate_content(prompt)

    return response.text