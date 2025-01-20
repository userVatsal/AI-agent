from flask import Flask, request, jsonify
from app.ai_code_assistant import AICodeAssistant
from app.ai_data_analyzer import AIDataAnalyzer
from app.ai_text_generator import AITextGenerator
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Initialize AI modules
ai_code_assistant = AICodeAssistant(api_key=os.getenv("OPENAI_API_KEY"))
ai_data_analyzer = AIDataAnalyzer(api_key=os.getenv("OPENAI_API_KEY"))
ai_text_generator = AITextGenerator(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/ai/code", methods=["POST"])
def ai_code_assistance():
    data = request.json
    prompt = data.get("prompt")
    language = data.get("language")
    response = ai_code_assistant.generate_code(prompt, language)
    return jsonify(response)

@app.route("/ai/analyze", methods=["POST"])
def ai_data_analysis():
    data = request.json
    dataset = data.get("dataset")
    question = data.get("question")
    response = ai_data_analyzer.analyze_data(dataset, question)
    return jsonify(response)

@app.route("/ai/text", methods=["POST"])
def ai_text_generation():
    data = request.json
    prompt = data.get("prompt")
    response = ai_text_generator.generate_text(prompt)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
