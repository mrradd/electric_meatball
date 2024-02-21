#This file contains the functions to read and write files.
import json

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
    with open(file_name, mode) as file:
        output = file.read()
    return output

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
    with open(file_name, mode) as file:
        file.write(text)