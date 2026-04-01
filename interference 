import os
import json
from openai import OpenAI

# Required environment variables (as per Meta OpenEnv Hackathon rules)
API_BASE_URL = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o")

client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URL,
)

SYSTEM_PROMPT = """You are EduAI – an AI Average Student Simulator.
Your role is to simulate how an average student would understand a teacher's lecture transcript.

Analyze the lecture and return a JSON object with the following structure:
{
  "understanding_score": <int 0-100>,
  "concept_clarity_score": <int 0-100>,
  "engagement_estimate": <int 0-100>,
  "difficulty_level": "<Easy|Medium|Hard>",
  "strengths": [<list of teacher strengths>],
  "weak_points": [<list of weak points>],
  "improvement_suggestions": [<list of suggestions>],
  "teaching_tips": [<list of tips>],
  "summary": "<brief overall feedback paragraph>"
}

Be honest, constructive, and simulate the perspective of an average student.
Return ONLY valid JSON, no extra text."""


def analyze_lecture(transcript: str) -> dict:
    """
    Analyzes a lecture transcript and returns evaluation scores and feedback.
    
    Args:
        transcript: The text of the teacher's lecture
        
    Returns:
        Dictionary containing scores, strengths, weak points, and suggestions
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        max_tokens=1000,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Please analyze this lecture transcript:\n\n{transcript}"}
        ]
    )

    result_text = response.choices[0].message.content.strip()

    # Clean up JSON if wrapped in markdown
    if result_text.startswith("```"):
        result_text = result_text.split("```")[1]
        if result_text.startswith("json"):
            result_text = result_text[4:]

    result = json.loads(result_text)
    return result


def run_inference(input_data: dict) -> dict:
    """
    Main inference entry point for the hackathon evaluator.
    
    Args:
        input_data: Dictionary with key 'transcript' containing lecture text
        
    Returns:
        EduAI evaluation result dictionary
    """
    transcript = input_data.get("transcript", "")

    if not transcript:
        return {"error": "No transcript provided. Please include a 'transcript' field."}

    result = analyze_lecture(transcript)
    return result


if __name__ == "__main__":
    # Example usage / smoke test
    sample_transcript = """
    Today we are going to learn about photosynthesis. 
    Plants use sunlight to make food. They take in carbon dioxide and water. 
    Then they produce glucose and oxygen. This process happens in the chloroplasts.
    The green color of plants comes from chlorophyll which absorbs sunlight.
    """

    test_input = {"transcript": sample_transcript}
    output = run_inference(test_input)
    print(json.dumps(output, indent=2))
