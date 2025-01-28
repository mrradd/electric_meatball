import json
from EMConstants import EM_CONFIG_FILE, MESSAGE, PROMPT_FILE_NAME, RESPONSE_ANSWER_FILE_NAME
from FileUtils import deserializeJsonFromFile, writeToFile, readFile
from ElectricMeatball import ElectricMeatball

class EMApp:
    """
    EMApp
    ---
    The main class for the Electric Meatball application.

    Instance Variables:
        ai_instance (ElectricMeatball): The instance of the ElectricMeatball class.
        clazz_name (str): The name of the class.
        configData (dict): The configuration data for the Electric Meatball application.
    """
    __instance = None
    
    def __new__(self):
        if self.__instance is None:
            self.__instance = super(EMApp, self).__new__(self)
        return self

    def initialize(self) -> None:
        """
        initialize
        ---
        This method sets the class name and initializes the ElectricMeatball instance.
        """
        self.__instance.clazz_name = "EMApp"
        self.__instance.configData = deserializeJsonFromFile(EM_CONFIG_FILE)
        self.__instance.ai_instance = ElectricMeatball().getInstance()
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
        response = self.__instance.ai_instance.performRequestFromPromptFileAndWriteToAnswerFile()
        # print("~Full response...~\n\n")
        # print(response)
        print("\n~FINISHED~")