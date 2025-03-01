import json
from EMConstants import EM_CONFIG_FILE, MESSAGE, PROMPT_FILE_NAME, RESPONSE_ANSWER_FILE_NAME
from FileUtils import deserializeJsonFromFile, writeToFile, readFile
from ElectricMeatballChat import ElectricMeatballChat

class EMCApp:
    """
    EMApp
    ---
    The main class for the Electric Meatball Chat application.

    Instance Variables:
        ai_instance (ElectricMeatballChat): The instance of the ElectricMeatballChat class.
        clazz_name (str): The name of the class.
        configData (dict): The configuration data for the Electric Meatball Chat application.
    """
    __instance = None
    
    def __new__(self):
        if self.__instance is None:
            self.__instance = super(EMCApp, self).__new__(self)
        return self

    def initialize(self) -> None:
        """
        initialize
        ---
        This method sets the class name and initializes the ElectricMeatballChat instance.
        """
        self.__instance.clazz_name = "EMCApp"
        self.__instance.configData = deserializeJsonFromFile(EM_CONFIG_FILE)
        self.__instance.ai_instance = ElectricMeatballChat().getInstance()
        self.__instance.ai_instance.initialize()

    @classmethod
    def getInstance(self):
        """
        getInstance
        ---
        Returns:
            The instance of the Rad API.
        """
        return self.__instance

    def printSelf(self):
        """
        printSelf
        ---
        Prints class info.
        """
        print(f"Class Name: {self.__instance.clazz_name}")
        self.__instance.ai_instance.printSelf()

    def run(self):
        # TODO CH  MAKE REQUEST response = self.__instance.ai_instance.performRequestFromPromptFileAndWriteToAnswerFile()
        # print("~Full response...~\n\n")
        # print(response)
        print("\n~FINISHED~")