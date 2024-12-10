# Speech-to-Text and PDF Generator

This Python script allows you to transcribe speech into text using either your microphone or an uploaded audio file. It then generates a PDF containing the transcribed text. The script also provides text-to-speech feedback for user interaction.

## Features

- **Microphone Input**: Records speech directly from your microphone.
- **Audio File Input**: Processes uploaded audio files (e.g., `.wav`).
- **Speech-to-Text**: Uses Google’s speech recognition API for transcription.
- **PDF Generation**: Creates a PDF file containing the transcribed text.
- **Text-to-Speech Feedback**: Provides auditory feedback during interaction.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  ```bash
  pip install SpeechRecognition pyttsx3 fpdf
