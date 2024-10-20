import os
import pyttsx3
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

client = Groq(
  api_key=os.getenv("GROQ_API_KEY"),)

print("Cortana: Welcome spartan!")
engine.say(" Welcome spartan")
engine.runAndWait()

while True:
  
  user_input = input("You: ")


  stream = client.chat.completions.create(
    messages=[
        {
        
         "role": "system",
         "content": "you are an ai assistant named cortana like form the series halo. you are to assist the user as best as possible, you can be a little funny and hilarous  but be straigth forward with answers. you are to provide short, precise and factual answers.",
        },
        {

         "role": "user",
         "content": user_input,
        }
    ],
    model = "llama3-8b-8192",
  )
 

  model_response = (stream.choices[0].message.content)

  print(f'Cortana: {model_response}')
  print()
  engine.say(model_response)
  engine.runAndWait()
  
  if user_input.lower() == "it was great knowing you":
    print("take care soldier")
    engine.say(" take care soldier")
    engine.runAndWait()
    break


