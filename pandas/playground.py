"""

    playground.py
    To test some stand alone methods before incorporate
    07/11/2024

"""

#
# Convert time delta to string containg Year, Months and days
#
from datetime import timedelta
import pandas as pd

def delta_to_string(delta):
    YEAR_DAYS = 365
    MONTH_DAYS = 30
    total_days = delta.days
    elapsed_years = total_days // YEAR_DAYS
    elapsed_months = (total_days % YEAR_DAYS) // MONTH_DAYS
    elapsed_days = (total_days % YEAR_DAYS) % MONTH_DAYS 
    str_ret = f"years: {elapsed_days}" if elapsed_years > 0 else ""
    str_ret = str_ret + f", " if len(str_ret) > 0 and elapsed_months > 0 else ""
    str_ret = str_ret + f"months: {elapsed_months}" if elapsed_months > 0 else ""
    str_ret = str_ret + f", " if len(str_ret) > 0 and elapsed_days > 0 else ""
    str_ret = str_ret + f"days: {elapsed_days}" if elapsed_days > 0 else ""
    return str_ret


vdelta = timedelta(days=397)

print(f"Original: {vdelta}, conversion: {delta_to_string(vdelta)}")

vdelta = timedelta(days=365//2)
print(f"Original: {vdelta}, conversion: {delta_to_string(vdelta)}")

vdelta = timedelta(days=15)
print(f"Original: {vdelta}, conversion: {delta_to_string(vdelta)}")