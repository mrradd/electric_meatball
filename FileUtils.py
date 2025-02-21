#This file contains the functions to read and write files.
import json

def deserializeJsonFromFile(file_name: str):
    """
    deserializeJsonFromFile
    ---
    Reads the content of a JSON file with the given file_name and deserializes it.

    Args:
        file_name (str)- The name of the JSON file to read.
    Returns:
        dict: Deserialized JSON.
    """
    output = "~NO JSON OUTPUT PROVIDED~"
    with open(file_name, "r") as file:
        output = json.load(file)
    return output

def insertTextAtBeginningOfFile(file_name: str, text_to_insert: str):
    """
    insertTextAtBeginningOfFile
    ---
    Prepends the given text to the beginning of the file with the given file_name.

    Args:
        file_name (str) - The name of the file to write to.\n
        text_to_insert (str) - The text to write to the file.\n
    """
    original_contents = readFile(file_name)

    new_contents = text_to_insert + "\n" + original_contents
    writeToFile(file_name, new_contents)

def insertTextAtEndOfFile(file_name: str, text_to_insert: str):
    """
    insertTextAtEndOfFile
    ---
    Appends the given text to the end of the file with the given file_name.

    Args:
        file_name (str) - The name of the file to write to.\n
        text_to_insert (str) - The text to write to the file.\n
    """
    new_contents = "\n" + text_to_insert
    writeToFile(file_name, new_contents, mode="a")

def readFile(file_name: str, mode: str = "r"):
    """
    readFile
    ---
    Reads the content of a file with the given file name and mode then returns it as a string.

    Args:
        file_name (str) - The name of the file to read.\n
        mode (str) - The mode to use when reading the file.\n
    Returns:
        str: The content of the file as a string.
    """
    output = "~NO OUTPUT PROVIDED~"
    with open(file_name, mode, encoding='utf-8') as file:
        output = file.read()
    return output

def writeToFile(file_name: str, text: str, mode: str = "w"):
    """
    writeToFile
    ---
    Writes the given text to a file with the given file_name using the given mode.

    Args:
        file_name (str) - The name of the file to write to.\n
        text (str) - The text to write to the file.\n
        mode (str) - The mode to use when writing to the file.\n
    """
    with open(file_name, mode, encoding='utf-8') as file:
        file.write(text)