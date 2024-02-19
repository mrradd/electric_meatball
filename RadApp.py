import json
from RadConstants import MESSAGE
from ai.RadAI import RadAI

class RadApp:
    """
    The RadAPI class represents the API for the Rad system.\n
    It provides methods for starting the API and getting the instance of the API.
    """
    __instance = None
    
    def __new__(self):
        if self.__instance is None:
            self.__instance = super(RadApp, self).__new__(self)
        return self

    def initialize(self) -> None:
        """
        This method sets the class name and initializes the RadAI instance.
        """
        self.__instance.clazz_name = "RadApp"
        self.__instance.ai_instance = RadAI().getInstance()
        self.__instance.ai_instance.initialize()

    @classmethod
    def getInstance(self):
        """
        Returns the instance of the Rad API.
        """
        return self.__instance

    def printSelf(self):
        print(f"Class Name: {self.__instance.clazz_name}")
        self.__instance.ai_instance.printSelf()

    @staticmethod
    def readTestPrompt():
        with open("TestPrompt.json") as json_data_file:
            return json.load(json_data_file)

    def run(self):
        self.__instance.initialize()
        prompt = RadApp.readTestPrompt()
        response = self.__instance.ai_instance.sendUserRequest(requestMessage = prompt[MESSAGE])
        RadApp.writeToFile("TestResponse2.txt", response.choices[0].message.content, "a")
        print(response)

    @staticmethod
    def writeToFile(file_name, text, mode = "w"):
        with open(file_name, mode) as file:
            file.write(text)
