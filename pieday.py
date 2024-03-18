from datetime import datetime
import csv
import math
import matplotlib.pyplot as plt

activities = []

# Open the CSV file
with open('pieday.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    # Iterate over each row in the CSV
    for row in reader:
        activity_name = row[0]
        start_time = datetime.strptime(row[1], '%I:%M %p')
        stop_time = datetime.strptime(row[2], '%I:%M %p')
        duration = float(row[3])
        activities.append((start_time, stop_time, activity_name, duration))

# Sort activities by start time
activities.sort()

# Colors for each slice
colors = ['#85C1E9', '#F5B041', '#A569BD', '#45B39D', '#52BE80', '#F1948A', '#BB8FCE', '#85C1E9', '#F7DC6F', '#A569BD', '#5DADE2', '#999999']

# Labels with activity name and start-stop times
labels = [f'{name}\n{start_time.strftime("%I:%M %p")}-{stop_time.strftime("%I:%M %p")}' for start_time, stop_time, name, _ in activities]

# Labels with activity name, start-stop times, and duration
# labels = [f'{name}\n{start_time.strftime("%I:%M %p")}-{stop_time.strftime("%I:%M %p")}\nDuration: {duration} hrs' for start_time, stop_time, name, duration in activities]

# Sizes for each slice
sizes = [duration for _, _, _, duration in activities]

# Create a single subplot with a larger size
fig, ax = plt.subplots(figsize=(12, 12))

# Adjust start angle to position midnight at the top, and draw the pie chart in a counterclockwise direction
ax.pie(sizes, colors=colors, startangle=-30, counterclock=False, labels=labels, labeldistance=1.1)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add lines and text for midnight, 6am, noon, 6pm, and 9pm
for hour, label in zip([0, 6, 12, 18, 15, 14.5, 13.5], ['Noon', '6AM', 'Midnight', '6PM', 'Screens Off\n9:00pm', 'Melatonin\n9:30pm', 'Lights Off\n10:30pm']):
    angle = (hour/24)*360 - 90  # Convert hours to angle in degrees, subtract 90 to start at the top
    angle = math.radians(angle)  # Convert angle to radians
    x = math.cos(angle)  # Calculate x coordinate
    y = math.sin(angle)  # Calculate y coordinate
    ax.plot([0, x], [0, y], color='darkgrey')  # Draw line from center to point in dark grey
    ax.text(0.9*x, 0.9*y, label, ha='center', va='center')  # Add text at point, moved a bit towards the center

# Rest of the code remains the same

# plt.show()

# Save the figure
fig.savefig("pieday.png")

# Save the figure with a tight bounding box
fig.savefig("pieday.png", bbox_inches='tight')