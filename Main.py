#This is the main file for the project which will be used to run the project.
from RadApp import RadApp

radAppInstance = RadApp().getInstance()

def main():
    radAppInstance.run()

main()