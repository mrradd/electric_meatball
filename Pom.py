import time
import os
import platform

# TODO CH  ALLOW FOR SETTING A DEFAULT TIME IN THE CONFIGURATION.
def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(500, 2000)  # Frequency (Hz), Duration (ms)
    else:
        os.system('echo -e "\a"')  # This may not work on all systems

def timer(minutes):
    total_seconds = minutes * 60
    print(f"Timer set for {minutes} minutes.")
    
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')   # Display countdown on the same line
        time.sleep(1)

    print("Time's up!")
    beep()

# Set the timer for a specified number of minutes
if __name__ == "__main__":
    try:
        minutes = int(input("Enter Pomodoro time in minutes: "))
        timer(minutes)
    except ValueError:
        print("Defaulting to 30 minutes.")
        timer(30)