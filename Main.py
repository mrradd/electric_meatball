#This is the main file for the project which is used to run the project.
from EMApp import EMApp

EMAppInstance = EMApp().getInstance()

def main():
    print("~STARTING Electric Meatball...~")
    EMAppInstance.initialize()
    EMAppInstance.run()
    print("~EXITING Electric Meatball...~")

main()