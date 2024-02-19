import json
from Constants import API_KEY, OPEN_AI

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
        Initialize the RadOpenAI instance.
        """
        with open("RadConfig.json") as json_data_file:
            data = json.load(json_data_file)
        
        self.__instance.clazz_name = "RadAI"
        self.__instance.api_key = data[OPEN_AI][API_KEY]

    @classmethod
    def getInstance(self):
        """
        Get the instance of RadOpenAI.

        Returns:
            RadOpenAI: The instance of RadOpenAI.
        """
        
        return self.__instance

    def connectToOpenAI(self):
        """
        Connect to the OpenAI API.
        """

    def printSelf(self):
        """
        Prints class info.
        """
        print(f"Class Name: {self.__instance.clazz_name}, API Key: {self.__instance.api_key}")