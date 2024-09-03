from datetime import datetime

def challenge2(timestamp: str) -> str:
  """
  Challenge 2
  Given a timestamp in 12-hour AM/PM format, convert it into 24-hour time in UTC with UTC date time
  format.
  
  Example
  Given the timestamp 05/05/2024 8:30AM, return 2024-05-05T08:30:00Z.
  """

  # Parse the month day, year, hours, minutes and AM/PM from the input
  twelveHour = datetime.strptime(timestamp, "%m/%d/%Y %I:%M%p")

  # Format the values in 24-hour UTC time
  twentyFourHour = twelveHour.strftime("%Y-%m-%dT%H:%M:%SZ")
  return twentyFourHour
