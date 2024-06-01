#return today date based on timezone in string format
def get_today_date():
    kolkata_tz = pytz.timezone('ASIA/Kolkata')
    # Get the current date in ASIA/Kolkata time zone
    today = date.today().strftime("%d/%m/%Y")
    today_kolkata = kolkata_tz.localize(datetime.strptime(today, "%d/%m/%Y")).strftime("%d/%m/%Y")
    return today_kolkata

def get_today_date_format():
    kolkata_tz = pytz.timezone('ASIA/Kolkata')
    # Get the current date in ASIA/Kolkata time zone
    today = datetime.now(tz=kolkata_tz).strftime("%Y-%m-%d")  # Get the date in YYYY-MM-DD format
    return today