
from openai import OpenAI
from datetime import datetime
from FileUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile, readFile, writeToFile
from EMConstants import API_KEY, CONTENT, MODEL, OPEN_AI, PROMPT_FILE_NAME, RESPONSE_ANSWER_FILE_NAME, ROLE, USER, EM_CONFIG_FILE, WRAP_TEXT_PROMPT

config_data = deserializeJsonFromFile(EM_CONFIG_FILE)
client = OpenAI(api_key = config_data[OPEN_AI][API_KEY])
prompt = readFile(file_name = config_data[PROMPT_FILE_NAME])

def generate_image(thePrompt):
  response = client.images.generate(
      model="dall-e-3",
      prompt=thePrompt,
      size="1024x1024",
      quality="hd",
      n=1,
  )
  print(response.data[0].url)

generate_image(prompt)