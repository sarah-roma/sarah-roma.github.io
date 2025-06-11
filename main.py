from datetime import datetime, timedelta

field = datetime(2025, 8, 10)
print(f'Future Event Date: {field.strftime('%B %d, %Y')}')

current_date = datetime.now()
remaining_time = field - current_date
print(f'Days until FIELD: {remaining_time.days}')

seconds_in_day = 86400
seconds_remaining = remaining_time.total_seconds()

hours, remainder = divmod(seconds_remaining, 3600)
minutes, seconds = divmod(remainder, 60)
days, remainder = divmod(hours, 24)

print(f'{int(days)} days, {int(hours % 24)} hours, {int(minutes)} minutes, {int(seconds)} seconds until FIELD')