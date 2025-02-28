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
    configData = deserializeJsonFromFile(HTTP_REQ_CONFIG_FILE)
    request_profile = config_profile_name

    url = configData[request_profile][URL]
    verb = configData[request_profile][VERB] #post, delete, push, etc...
    file_path = configData[DATA_DUMP_FILE_PATH]
    json_indent = configData[PRETTY_JSON_INDENT]

    verb = verb.lower()
    if verb == GET.lower() :
      http_response = requests.get(url)
    if verb == POST.lower() :
      http_response = requests.post(url, None, configData[request_profile][BODY])
    else :
      print("[" + verb + "] is not supported.\nExiting")
      sys.exit()

    request_delimiter = "~~~~~~~~~~~~~~~~~~~~| " + request_profile + " | " + str(datetime.now()) + " |~~~~~~~~~~~~~~~~~~~~"

    print(http_response.status_code)
    insertTextAtEndOfFile(file_path, request_delimiter)
    insertTextAtEndOfFile(
      file_path, json.dumps(http_response.json(), indent=json_indent) #This pretty prints the json.
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
  returns: The response from the HTTP request.
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

#Do the thing.
do_http_request(profile_to_run)