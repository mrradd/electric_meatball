
from openai import OpenAI
from datetime import datetime
from FileUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile, readFile, writeToFile
from EMConstants import API_KEY, IMAGE_URL_DUMP_FILE, OPEN_AI, PROMPT_FILE_NAME, EM_CONFIG_FILE
from EMConstants import IMAGE_DIMENSIONS, IMAGE_MODEL, IMAGE_QUALITY, NUMBER_OF_IMAGES_TO_GENERATE

def generate_image():
  config_data = deserializeJsonFromFile(EM_CONFIG_FILE)
  file_name = config_data[PROMPT_FILE_NAME]
  answer_file_name = config_data[IMAGE_URL_DUMP_FILE]
  client = OpenAI(api_key = config_data[OPEN_AI][API_KEY])
  prompt = readFile(file_name)
  dimensions = config_data[IMAGE_DIMENSIONS]
  image_quality = config_data[IMAGE_QUALITY]
  image_model = config_data[IMAGE_MODEL]
  number_of_images = config_data[NUMBER_OF_IMAGES_TO_GENERATE]

  print("~Sending the request.~")
  response = client.images.generate(
    model=image_model,
    prompt=prompt,
    size=dimensions,
    quality=image_quality,
    n=number_of_images,
  )

  request_time = str(datetime.now())
  print("~Writing response to file, '" + answer_file_name + "'~")
  print("~"+ request_time +"~")
  prompt_text_to_save = "Prompt:\n------\n" + prompt + "\n\n--------\n"
  answer_text_to_save = "Answer:\n------\n" + response.data[0].url
  text_to_save = "\n------RESPONSE START------ "+ request_time +"\n" + prompt_text_to_save + answer_text_to_save + "\n------RESPONSE END------\n"
  all_text = text_to_save + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
  insertTextAtBeginningOfFile(answer_file_name, all_text)

generate_image()