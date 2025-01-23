import time
import os
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 2000)  # Frequency (Hz), Duration (ms)
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
        minutes = int(input("Enter Pomodoro session time in minutes: "))
        timer(minutes)
    except ValueError:
        print("Please enter a valid number.")