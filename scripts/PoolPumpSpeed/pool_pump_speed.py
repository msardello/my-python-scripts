import datetime
from datetime import datetime, timedelta

low_allocation = .65
med_allocation = .20
high_allocation = .15

def calc_pump_hours(run_hrs, pump_speed):
    if pump_speed == "low":
        return int(round(low_allocation * run_hrs, 0))
    elif pump_speed == "med":
        return int(round(med_allocation * run_hrs, 0))
    elif pump_speed == "high":
        return int(round(high_allocation * run_hrs,0))

# Function to add hours to a specific time
def add_hours_to_time(hours, start_time):
    # Create a datetime object for the start time (8:30 AM)
    time_format = "%I:%M %p"  # Format for 12-hour time with AM/PM
    start_time_obj = datetime.strptime(start_time, time_format)
    # Add the specified number of hours
    new_time = start_time_obj + timedelta(hours=hours)
    return new_time.strftime("%I:%M %p")

average_high_temp = int(input(f"What is the average high temperature this month?: "))
start_time = input(f"What time would you like to start your pump? (enter HH:MM AM/PM): ")
run_hrs = round(average_high_temp / 10, 0)
speeds = {
    "low":1350,
    "med":2070,
    "high":2935
}

print(f"Since the average high temperature is {average_high_temp}, you should run your pump for {run_hrs} hours.")

# for speed in speeds.keys():
for speed in speeds:
    speed_hours = calc_pump_hours(run_hrs, speed)
    hours_to_add = speed_hours
    end_time = add_hours_to_time(hours_to_add, start_time)
    print(f"You should run your pump at {speeds[speed]} RPMs for approximately {speed_hours} hours from {start_time} to {end_time}")
    start_time = end_time





