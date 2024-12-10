import speech_recognition as sr
import pyttsx3
from fpdf import FPDF
import os

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def convert_to_text_from_mic():
    recognizer = sr.Recognizer()
    text_collected = []

    print("Listening... Speak now! Say 'stop' to end recording.")
    text_to_speech("Listening... Speak now! Say 'stop' to end recording.")

    with sr.Microphone() as source:
        while True:
            try:
                print("You can speak now...")
                audio = recognizer.listen(source, timeout=10)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                if "stop" in text.lower():
                    print("Stopping recording.")
                    text_to_speech("Stopping recording.")
                    break
                text_collected.append(text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio. Please try again.")
                text_to_speech("Sorry, I could not understand the audio. Please try again.")
            except sr.RequestError:
                print("Could not request results, please check your internet connection.")
                text_to_speech("Could not request results, please check your internet connection.")
                break

    return " ".join(text_collected)

def convert_to_text_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Processing audio file...")
        text_to_speech("Processing audio file...")
        try:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("Transcription:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
            return None

def save_text_to_pdf(text, output_path="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)
    print(f"PDF saved as {output_path}")
    text_to_speech(f"PDF saved as {output_path}")

def main():
    print("Choose input method:\n1. Microphone\n2. Audio File")
    text_to_speech("Choose input method: 1 for microphone, or 2 for audio file.")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        text = convert_to_text_from_mic()
    elif choice == "2":
        file_path = input("Enter the path to the audio file: ")
        if os.path.exists(file_path):
            text = convert_to_text_from_file(file_path)
        else:
            print("File not found. Please check the path.")
            return
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    if text:
        save_text_to_pdf(text)
    else:
        print("No text to save.")

if __name__ == "__main__":
    main()
