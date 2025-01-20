import openai

class AITextGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative writer."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"text": response.choices[0].message["content"]}
