from datetime import datetime, timedelta, date

now = datetime.now()

# # Create a specific date and time (YYYY, MM, DD, HH, MM, SS)
# specific_datetime = datetime(2024, 12, 25, 18, 30, 45)
# print(specific_datetime)  # Output: 2024-12-25 18:30:45

# Example: Format as 'Day-Month-Year Hour:Minute'
# formatted_date = now.strftime("%d-%m-%Y %H:%M")
# print(formatted_date)  # Example: 18-10-2024 14:32

# date_str = "25-12-2024 18:30"
# parsed_date = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
# print(parsed_date)  # Output: 2024-12-25 18:30:00


# from datetime import timedelta
#
# # Add 5 days to the current date
# new_date = now + timedelta(weeks=5)
# print(new_date)  # Example: 2024-10-23
#
# # Subtract 2 hours from the current time
# new_time = now - timedelta(hours=2)
# print(new_time)  # Example: 2024-10-18 12:32:10
#
#
# today = date.today()
# print(today)
# from datetime import datetime
#
# # Convert epoch seconds to a datetime object
# timestamp = datetime.fromtimestamp(0)
# print(timestamp)  # Output: 1970-01-01 00:00:00
#

