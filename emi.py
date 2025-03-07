
from openai import OpenAI
from datetime import datetime
from FileUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile, readFile, writeToFile
from EMConstants import API_KEY, OPEN_AI, PROMPT_FILE_NAME, EM_CONFIG_FILE
from EMConstants import IMAGE_DIMENSIONS, IMAGE_MODEL, IMAGE_QUALITY, NUMBER_OF_IMAGES_TO_GENERATE

config_data = deserializeJsonFromFile(EM_CONFIG_FILE)

client = OpenAI(api_key = config_data[OPEN_AI][API_KEY])
dimensions = config_data[IMAGE_DIMENSIONS]
image_quality = config_data[IMAGE_QUALITY]
image_model = config_data[IMAGE_MODEL]
number_of_images = config_data[NUMBER_OF_IMAGES_TO_GENERATE]
prompt = readFile(file_name = config_data[PROMPT_FILE_NAME])

def generate_image():
  """
  Generates an image based on the user's prompt and the defined configuration file then prints the
  image's url to the console. Use the url to view the image.
  
  For more info https://platform.openai.com/docs/guides/images.
  """
  response = client.images.generate(
      model=image_model,
      prompt=prompt,
      size=dimensions,
      quality=image_quality,
      n=number_of_images,
  )
  print(response.data[0].url)

generate_image()