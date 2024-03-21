import pyautogui as screen
import random
import time
import psutil
from datetime import datetime
import pytz

pyautogui.FAILSAFE = False
sleep_time = 45  # 45 seconds
value = 6000
check_interval = 10  # seconds, configurable check interval
enable_time_check = True  # Set to False to disable time-based checks

# Define time range (9 AM to 5:30 PM Eastern time)
start_hour = 9
start_minute = 0
end_hour = 17
end_minute = 30

# Define timezone
eastern = pytz.timezone('US/Eastern')

x, y = screen.size()

def is_within_time_range():
    now = datetime.now(eastern)
    start_time = now.replace(hour=start_hour, minute=start_minute)
    end_time = now.replace(hour=end_hour, minute=end_minute)
    return start_time <= now <= end_time

counter = 0
while True and counter < value:
    # Print current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time:", current_time)

    if enable_time_check:
        if not is_within_time_range():
            print("Outside of specified time range. Script will sleep.")
            time.sleep(60)  # Sleep for a minute
            continue

    # Perform action for every check
    print("Performing action for every check...")

    # Get system idle time using psutil
    cpu_times = psutil.cpu_times()
    idle_time = cpu_times.idle
    
    if idle_time < 10:  # Adjust the threshold as needed
        print("System is being used.")
        # Do something when system is being used
    else:
        print("System is idle. Moving cursor.")
        x1 = random.randint(0, x)
        y1 = random.randint(0, y)
        screen.moveTo(x1, y1)
        screen.click(int(x/2), y - 30)
        x1 = random.randint(0, x)
        y1 = random.randint(0, y)
        screen.moveTo(x1, y1)
        screen.click(int(x/2), y-30)
        
    # Wait for the configured interval before checking again
    time.sleep(check_interval)
    counter += 1
