import shutil
import os
from pydub import AudioSegment
import speech_recognition as sr

class SpeechService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def extract_audio(self, video_file_path, audio_file_path):
        """Extract audio from a video file and save it as an audio file."""
        try:
            audio = AudioSegment.from_file(video_file_path)
            audio.export(audio_file_path, format="wav")
            print(f"Audio extracted and saved to {audio_file_path}")
        except Exception as e:
            print(f"Error extracting audio: {e}")

    def speech_to_text(self, audio_file_path):
        """Convert spoken language in an audio file to text."""
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                print(f"Recognized text: {text}")
                return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
