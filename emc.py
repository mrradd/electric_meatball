#This is the main file for the project which is used to run the EMCApp.
from EMCApp import EMCApp

EMCAppInstance = EMCApp().getInstance()

def main():
    print("~STARTING Electric Meatball...~")
    EMCAppInstance.initialize()
    EMCAppInstance.run()
    print("~EXITING Electric Meatball...~")

main()