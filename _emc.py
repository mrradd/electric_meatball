from openai import OpenAI
from datetime import datetime
from FileUtils import deserializeJsonFromFile, writeToFile, readFile
from EMConstants import API_KEY, CONTENT, MODEL, OPEN_AI, PROMPT_FILE_NAME, CHAT_FILE_NAME, ROLE, USER, EM_CONFIG_FILE
import json

config_data = deserializeJsonFromFile(EM_CONFIG_FILE)
client = OpenAI(api_key = config_data[OPEN_AI][API_KEY])

def main():
    data = send_user_request()
    writeToFile(config_data[CHAT_FILE_NAME], json.dumps(data, indent=2))
    print(data[-1]["api_response"]["output"][0]["content"][0]["text"])

def send_user_request():
    """
    Sends a user request message to the OpenAI Response API.

    Returns:
        Object: JSON object based on the response from the ChatGPT Response API.
    """
    model = config_data[OPEN_AI][MODEL]
    prompt = readFile(file_name = config_data[PROMPT_FILE_NAME])
    date = str(datetime.now())
    messages = [{ROLE: USER, CONTENT: prompt}]

    prev_resps = []
    from_file = readFile(config_data[CHAT_FILE_NAME])
    # We have previous responses, so add the latest response id to the chat.
    if len(from_file) > 0:
        prev_resps = json.loads(from_file)

    if len(prev_resps) <= 0:
        response = client.responses.create(
            model = model,
            input = messages
        )
    else:
        response = client.responses.create(
            model = model,
            input = messages,
            previous_response_id = prev_resps[-1]["api_response"]["id"]
        )

    resps = []
    resp = {
        "date": date,
        "prompt": prompt,
        "api_response": response.to_dict(use_api_names=False, mode="json")
    }

    if len(from_file) > 0:
        resps = prev_resps[:]

    resps.append(resp)

    return resps

main()