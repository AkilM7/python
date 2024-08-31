from datetime import datetime, timedelta
import time

# Set the future date and time
future_date = datetime(2024, 12, 31,23, 59, 59)

while True:
    # Get the current time
    now = datetime.now()
    
    # Calculate the difference
    remaining_time = future_date - now
    
    # Break the loop if the countdown is over
    if remaining_time.total_seconds() <= 0:
        print("Countdown complete!")
        break
    
    # Clear the screen and print remaining time
    print(f"Time left: {remaining_time}", end='\r')
    
    # Wait for a second before updating
    time.sleep(0)

