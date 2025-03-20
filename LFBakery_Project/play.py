from datetime import datetime

now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date_time)
