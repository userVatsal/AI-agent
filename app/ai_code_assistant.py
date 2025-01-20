import openai

class AICodeAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_code(self, prompt, language):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a coding assistant. Generate code in {language}."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"code": response.choices[0].message["content"]}
