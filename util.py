from datetime import datetime

def YearsFromToday(x):
        today = datetime.today().date()
        dayFrom = today.replace(year=today.year - x)
        return dayFrom