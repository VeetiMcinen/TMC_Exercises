from datetime import date
def list_years(dates:list):
    years = []
    for i in sorted(dates):
        year = i.year
        years.append(year)
    return years



