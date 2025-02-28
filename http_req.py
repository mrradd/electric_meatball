from datetime import datetime
import requests, json, sys
from FileUtils import deserializeJsonFromFile, insertTextAtEndOfFile
from http_req_constants import HTTP_REQ_CONFIG_FILE, BODY, URL, VERB, DATA_DUMP_FILE_PATH, PRETTY_JSON_INDENT, GET, POST

#~~~Set this to the profile to run~~~
profile_to_run = "test_post"

###################################################################################################

def do_http_request(config_profile_name):
  """
  do_http_request
  ---
  Performs an http request based on the specified configuration profile name in the config file,
  `http_req_config.json`. The data from the response is appended to the file specified by the
  config property, `data_dump_file_path`.
  ---
  params:
    - `config_profile_name` (str): The name of the object in the configuration's json object to use
    for the request.
  """
  try:
    config_data = deserializeJsonFromFile(HTTP_REQ_CONFIG_FILE)

    http_response = handle_request(config_data[config_profile_name])

    file_path = config_data[DATA_DUMP_FILE_PATH]
    request_delimiter = response_dump_delimiter(config_profile_name)

    print(http_response.status_code)
    insertTextAtEndOfFile(file_path, request_delimiter)
    
    #This writes pretty printed json to the dump file.
    insertTextAtEndOfFile(
      file_path, json.dumps(http_response.json(), indent=config_data[PRETTY_JSON_INDENT])
    )
    print("Data written to [" + file_path +"]")

  except requests.exceptions.Timeout as e:
    print("$$$ Timeout")
    raise SystemExit(e)
  except requests.exceptions.TooManyRedirects as e:
    print("$$$ Too many redirects")
    raise SystemExit(e)
  except requests.exceptions.RequestException as e:
    print("$$$ The world is on fire!!!")
    raise SystemExit(e)
  except Exception as e:
    print("You broke it not me.")
    raise SystemExit(e)

###################################################################################################

def handle_request(profile_object):
  """
  handle_request
  ---
  Performs the http request based on the passed in `profile_object` that was read in from
  `http_req_config.json`.
  ---
  params:
    - `profile_object` (object): The object containing information about the request to 
    perform.
  ---
  returns: `string` - The response from the HTTP request.
  """
  http_response = ""
  try:
    url = profile_object[URL]
    verb = profile_object[VERB].lower()
    if verb == GET.lower():
      http_response = requests.get(url)
    if verb == POST.lower():
      http_response = requests.post(url, None, profile_object[BODY])
    else:
      print("[" + verb + "] is not supported.\nExiting")
      sys.exit()
    return http_response
  except Exception as e:
    raise SystemExit(e)

###################################################################################################

def response_dump_delimiter(config_profile_name):
  """
  response_dump_delimiter
  ---
  Creates a delimiter for separating the request responses in the dump file.
  ---
  params:
    - `config_profile_name` (string): Name of the profile the response if from.
    perform.
  ---
  returns: `string` - The delimiter to write to the file.
  """
  return "~~~~~~~~~~~~~~~~~~~~| " + config_profile_name + " | " + str(datetime.now()) + " |~~~~~~~~~~~~~~~~~~~~"

###################################################################################################

#Do the thing.
do_http_request(profile_to_run)