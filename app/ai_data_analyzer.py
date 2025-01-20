import openai
import pandas as pd

class AIDataAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_data(self, dataset, question):
        df = pd.read_csv(dataset)
        summary = df.describe().to_string()

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data analyst. Analyze the dataset and answer the user's question."},
                {"role": "user", "content": f"Dataset Summary:\n{summary}\n\nQuestion: {question}"}
            ]
        )
        return {"analysis": response.choices[0].message["content"]}
