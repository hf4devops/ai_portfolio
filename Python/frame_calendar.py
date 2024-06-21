import pandas as pd
from datetime import datetime, timedelta

def generate_timeframes(start_date: str, end_date: str) -> list:
    """
    Generates a list of dictionaries with date, day of the week, and week number.

    Parameters:
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    list: A list of dictionaries containing date, day of the week, and week number.
    """
    # Parse the input dates
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Generate the date range
    date_range = pd.date_range(start=start_date, end=end_date)

    # Create the time frames
    timeframes = []
    for date in date_range:
        day_of_week = date.strftime('%A')
        week_number = date.isocalendar()[1]
        timeframes.append({
            'date': date.strftime('%Y-%m-%d'),
            'day_of_week': day_of_week,
            'week_number': week_number
        })

    return timeframes

# Example usage
start_date = '2023-05-15'
end_date = '2023-06-19'
timeframes = generate_timeframes(start_date, end_date)

# Display the generated timeframes
for timeframe in timeframes:
    print(timeframe)
