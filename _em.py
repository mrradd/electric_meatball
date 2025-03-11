from openai import OpenAI
from datetime import datetime
from FileUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile, readFile
from EMConstants import API_KEY, CONTENT, MODEL, OPEN_AI, PROMPT_FILE_NAME, RESPONSE_ANSWER_FILE_NAME, ROLE, USER, EM_CONFIG_FILE

config_data = deserializeJsonFromFile(EM_CONFIG_FILE)
client = OpenAI(api_key = config_data[OPEN_AI][API_KEY])

def main():
    chat_response = send_request_and_write_to_file()

def generate_user_message(content: str):
    """
    Generate a user message with the given content.

    Args:
        content (str): The content of the user message.

    Returns:
        list: A list containing a dictionary representing the user message.
    """
    return [{ROLE: USER, CONTENT: content}]

def send_request_and_write_to_file():
    """
    performRequestFromPromptFileAndWriteToAnswerFile
    ---
    Reads the prompt text from the prompt file, performs a request, then writes the response to the answer file.

    Returns:
        dict: The response from the OpenAI chat model.
    """
    print("~Reading prompt file.~")
    prompt = readFile(file_name = config_data[PROMPT_FILE_NAME])
    answer_file_name = config_data[RESPONSE_ANSWER_FILE_NAME]
    
    print("~Sending the request.~")
    request_time = str(datetime.now())
    response = send_user_request()

    print("~Writing response to file, '" + answer_file_name + "'~")
    print("~"+ request_time +"~")
    prompt_text_to_save = "Prompt:\n------\n" + prompt + "\n\n--------\n"
    answer_text_to_save = "Answer:\n------\n" + response.choices[0].message.content
    text_to_save = "\n------RESPONSE START------ "+ request_time +"\n" + prompt_text_to_save + answer_text_to_save + "\n------RESPONSE END------\n"
    all_text = text_to_save + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    insertTextAtBeginningOfFile(answer_file_name, all_text)
    return response

def send_user_request():
    """
    Sends a user request message to the OpenAI chat model and returns the response.

    Returns:
        dict: The response from the OpenAI chat model.
    """
    model = config_data[OPEN_AI][MODEL]
    prompt = readFile(file_name = config_data[PROMPT_FILE_NAME])
    messages = generate_user_message(prompt)
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    return response

main()