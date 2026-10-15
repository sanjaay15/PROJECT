import pytesseract
from PIL import Image
from gtts import gTTS
from io import BytesIO
import playsound
from IPython import get_ipython
from IPython.display import display, Audio

def text_to_speech(text):
  tts=gTTS(text=text,lang='en',slow=False)
  audio_stream =BytesIO()
  tts.write_to_fp(audio_stream)
  audio_stream.seek(0)
  return audio_stream

def save_audio(audio_stream,file_name):
  with open(file_name,'wb') as f:
    f.write(audio_stream.read())
    audio_stream.close()
  print(f"Audio saved as {file_name}")

def image_to_text (image_path):
  try:
    image  = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
  except Exception as e:
    print(f"Error: {e}")
    return None
if __name__ == "__main__":
  image_path="/content/SAMPLE2.png"
  extracted_text = image_to_text(image_path)
print("Extracted Text:")
print(extracted_text)

if __name__ =="__main__":
  audio_stream=text_to_speech(extracted_text)
  file_name="text_to_speech_output.mp3"
  save_audio(audio_stream,file_name)
  display(Audio(file_name))

