from openai import OpenAI
from datetime import datetime
from EMUtils import deserializeJsonFromFile, insertTextAtBeginningOfFile, readFile, writeToFile
from EMConstants import API_KEY, CONTENT, MODEL, OPEN_AI, PROMPT_FILE_NAME, RESPONSE_ANSWER_FILE_NAME, ROLE, USER, EM_CONFIG_FILE

class ElectricMeatball:
    """
    ElectricMeatball
    ---
    A singleton class representing the ElectricMeatball instance.

    Instance Variables:
        clazz_name (str): The name of the class.
        client (OpenAI): The OpenAI client.
        configData (dict): The configuration data for the Electric Meatball application.
    """
    __instance = None

    def __new__(self):
        if self.__instance is None:
            self.__instance = super(ElectricMeatball, self).__new__(self)
        return self
    
    def initialize(self) -> None:
        """
        initialize
        ---
        Initializes the ElectricMeatball instance by loading configuration data from EMConfig.json.
        and setting up the OpenAI client.
        """
        self.__instance.configData = deserializeJsonFromFile(EM_CONFIG_FILE)
        self.__instance.clazz_name = "ElectricMeatball"
        self.__instance.client = OpenAI(api_key = self.__instance.configData[OPEN_AI][API_KEY])

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

    @classmethod
    def getInstance(self):
        """
        Get the instance of ElectricMeatball.

        Returns:
            ElectricMeatball: The instance of ElectricMeatball.
        """
        return self.__instance

    def performRequestFromPromptFileAndWriteToAnswerFile(self):
        """
        performRequestFromPromptFileAndWriteToAnswerFile
        ---
        Reads the prompt text from the prompt file, performs a request, then writes the response to the answer file.

        Returns:
            dict: The response from the OpenAI chat model.
        """
        print("~Reading prompt file.~")
        prompt = readFile(file_name = self.__instance.configData[PROMPT_FILE_NAME])
        
        print("~Sending the request.~")
        request_time = str(datetime.now())
        response = self.__instance.sendUserRequest(prompt)

        print("~Writing response to answer file.~")
        print("~"+ request_time +"~")
        prompt_text_to_save = "Prompt:\n------\n" + prompt + "\n\n--------\n"
        answer_text_to_save = "Answer:\n------\n" + response.choices[0].message.content
        text_to_save = "\n------RESPONSE START------ "+ request_time +"\n" + prompt_text_to_save + answer_text_to_save + "\n------RESPONSE END------\n"
        derp = text_to_save + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        insertTextAtBeginningOfFile(self.__instance.configData[RESPONSE_ANSWER_FILE_NAME], derp)
        return response

    def printSelf(self):
        """
        printSelf
        ---
        Prints class info.
        """
        print(f"Class Name: {self.__instance.clazz_name}, API Key: {self.__instance.api_key}")

    def sendUserRequest(self, requestMessage: str):
        """
        Sends a user request message to the OpenAI chat model and returns the response.

        Args:
            requestMessage (str): The user request message.

        Returns:
            dict: The response from the OpenAI chat model.
        """
        model = self.__instance.configData[OPEN_AI][MODEL]
        messages = self.generateUserMessage(requestMessage)
        response = self.__instance.client.chat.completions.create(
            model = model,
            messages = messages
        )
        return response