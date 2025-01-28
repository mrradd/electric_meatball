import time
import os
import platform
from datetime import datetime

# TODO CH  ALLOW FOR SETTING A DEFAULT TIME IN THE CONFIGURATION.
def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(500, 2000)  # Frequency (Hz), Duration (ms)
    else:
        os.system('echo -e "\a"')  # This may not work on all systems

def printFormattedDateTimeNow()
    now = datetime.now()
    formatted_datetime = now.strftime("Started: %Y-%m-%d %H:%M:%S")
    print(formatted_datetime)    

def timer(minutes):
    total_seconds = minutes * 60
    print(f"Timer set for {minutes} minutes.")    
    printFormattedDateTimeNow()
    
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')   # Display countdown on the same line
        time.sleep(1)

    print("Time's up!")
    printFormattedDateTimeNow()
    beep()


# Set the timer for a specified number of minutes
if __name__ == "__main__":
    try:
        minutes = int(input("Enter Pomodoro time in minutes: "))
        timer(minutes)
    except ValueError:
        # Defaulting to 30 minutes, because that's a normal session for me.
        timer(30)