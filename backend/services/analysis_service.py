import openai

class AnalysisService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_lecture(self, lecture_transcript):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Replace with your desired model
                messages=[
                    {
                        "role": "user",
                        "content": f"Please analyze the following lecture transcript and provide key points and insights: {lecture_transcript}",
                    }
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error during analysis: {str(e)}"