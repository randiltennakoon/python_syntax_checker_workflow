from datetime import date, datetime


from datetime import datetime

today = datetime.today()
deadline = '21.04.2022'
deadline = datetime.strptime(deadline, '%d.%m.%Y')

remaining_days = deadline - today
print(f'Days left: {remaining_days.days}')