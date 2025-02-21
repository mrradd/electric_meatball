from datetime import datetime
import requests, json, sys
from FileUtils import deserializeJsonFromFile, insertTextAtEndOfFile
from http_req_constants import HTTP_REQ_CONFIG_FILE, BODY, URL, VERB, DATA_DUMP_FILE_PATH, PRETTY_JSON_INDENT


def do_http_request(config_profile_name):
  """
  do_http_request
  ---
  Performs an http request based on the specified configuration profile name in the config file,
  `http_req_config.json`. The data from the response is appended to the file specified by the
  config property, `data_dump_file_path`.
  ---
  params:
    - `config_profile_name` (str): The name of the object in the configuration's json object to use for
    the request.
  """
  configData = deserializeJsonFromFile(HTTP_REQ_CONFIG_FILE)
  request_profile = config_profile_name

  # Can change these in http_req_config.json.
  url = configData[request_profile][URL]
  verb = configData[request_profile][VERB] #post, delete, push, etc...
  file_path = configData[DATA_DUMP_FILE_PATH]
  json_indent = configData[PRETTY_JSON_INDENT]

  http_response = ""
  try:
    date_time_str = str(datetime.now())
    request_delimiter = "\n~~~~~~~~~~~~~~~~~~~~~| "+ date_time_str + " |~~~~~~~~~~~~~~~~~~~~~\n"
    verb = verb.lower()
    
    if verb == "get" :
      http_response = requests.get(url)
    else :
      print("[" + verb + "] is not supported.\nExiting")
      sys.exit()
    
    print(http_response.status_code)
    insertTextAtEndOfFile(file_path, request_delimiter)
    insertTextAtEndOfFile(
      file_path, json.dumps(http_response.json(), indent=json_indent)
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

  except:
    print("You broke it not me.")

#Do the thing.
profile_to_run = "get_thing"
do_http_request(profile_to_run)