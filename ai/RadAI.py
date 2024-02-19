import json
from openai import OpenAI
from RadConstants import API_KEY, CONTENT, JSON_OBJECT, MODEL, OPEN_AI, ORGANIZATION, ROLE, USER, TYPE

class RadAI:
    """
    A singleton class representing the RadOpenAI instance.
    """
    __instance = None

    def __new__(self):
        if self.__instance is None:
            self.__instance = super(RadAI, self).__new__(self)
        return self
    
    def initialize(self) -> None:
        """
        Initializes the RadAI instance by loading configuration data from RadConfig.json
        and setting up the OpenAI client.

        Raises:
            FileNotFoundError: If RadConfig.json file is not found.
            KeyError: If the API key is not found in the configuration data.
        """
        with open("RadConfig.json") as json_data_file:
            self.__instance.configData = json.load(json_data_file)
        self.__instance.clazz_name = "RadAI"
        self.__instance.client = OpenAI(api_key=self.__instance.configData[OPEN_AI][API_KEY])

    @classmethod
    def getInstance(self):
        """
        Get the instance of RadOpenAI.

        Returns:
            RadOpenAI: The instance of RadOpenAI.
        """
        return self.__instance

    def sendUserRequest(self, requestMessage: str):
        """
        Sends a user request message to the OpenAI chat model and returns the response.

        Args:
            requestMessage (str): The user request message.

        Returns:
            dict: The response from the OpenAI chat model.
        """
        model = self.__instance.configData[OPEN_AI][MODEL]
        messages = RadAI.generateUserMessage(requestMessage)

        response = self.__instance.client.chat.completions.create(
            model=model,
            messages=messages
        )

        return response

    @staticmethod
    def generateUserMessage(content: str):
        """
        Generate a user message with the given content.

        Args:
            content (str): The content of the user message.

        Returns:
            list: A list containing a dictionary representing the user message.
        """
        return [{ROLE: USER, CONTENT: content}]

    def printSelf(self):
        """
        Prints class info.
        """
        print(f"Class Name: {self.__instance.clazz_name}, API Key: {self.__instance.api_key}")