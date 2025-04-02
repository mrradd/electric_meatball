from datetime import datetime
import requests, json, sys
from FileUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile
from http_req_constants import HTTP_REQ_CONFIG_FILE, BODY, REQUEST_TO_EXECUTE, URL, VERB
from http_req_constants import DATA_DUMP_FILE_PATH, PRETTY_JSON_INDENT, GET, POST

###################################################################################################

def do_http_request():
  """
  do_http_request
  ---
  Performs an http request based on the specified configuration's `request_to_execute` value in the
  config file, `http_req_config.json`. The data from the response is appended to the file specified
  by the config property, `data_dump_file_path`.
  """
  try:
    config_data = deserializeJsonFromFile(HTTP_REQ_CONFIG_FILE)
    req_to_exec = config_data[REQUEST_TO_EXECUTE]
    http_response = handle_request(config_data[req_to_exec])
    file_path = config_data[DATA_DUMP_FILE_PATH]
    request_delimiter = response_dump_delimiter(req_to_exec)
    print(http_response.status_code)

    #This writes pretty printed json to the dump file.
    insertTextAtBeginningOfFile(
      file_path, json.dumps(http_response.json(), indent=config_data[PRETTY_JSON_INDENT])
    )
    insertTextAtBeginningOfFile(file_path, request_delimiter)

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
  
  params:
    - `profile_object` (object): The object containing information about the request to 
    perform.
  
  - returns: `string` - The response from the HTTP request.
  """
  http_response = ""
  try:
    url = profile_object[URL]
    verb = profile_object[VERB].lower()
    if verb == GET.lower():
      http_response = requests.get(url)
    elif verb == POST.lower():
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

  params:
    - `config_profile_name` (string): Name of the profile the response if from.
    perform.
  
  - returns: `string` - The delimiter to write to the file in order to separate the requests for
    better readablility.
  """
  return "~~~~~~~~~~~~~~~~~~~~| Request Profile: `" + config_profile_name + "` | " + str(datetime.now()) + " |~~~~~~~~~~~~~~~~~~~~"

###################################################################################################

#Do the thing.
do_http_request()