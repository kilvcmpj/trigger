import pyautogui as screen
import random
import time
import psutil

screen.FAILSAFE = False
sleep_time = 45  # 45 seconds
check_interval = 10  # seconds
value = 6000

x, y = screen.size()

counter = 0
while counter < value:
    start_time = time.time()  # Start time of the loop
    while True:
        # Get system idle time using psutil
        cpu_times = psutil.cpu_times()
        idle_time = cpu_times.idle
        
        if idle_time < 10:  # Adjust the threshold as needed
            print("System is being used.")
            # Do something when system is being used
            break  # Exit the inner loop if system is being used
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
        
        # Wait for the specified interval before checking again
        time.sleep(check_interval)
        
        # Calculate the elapsed time since the start of the loop
        elapsed_time = time.time() - start_time
        
        # If the elapsed time exceeds the sleep_time, break the inner loop
        if elapsed_time >= sleep_time:
            break
    
    # Wait for the remaining time in the loop
    time.sleep(sleep_time - elapsed_time)
    
    counter += 1
