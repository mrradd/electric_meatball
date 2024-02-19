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