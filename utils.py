import datetime

def get_date():
    """Get the current date in YYYY-MM-DD format
    
    :return: current date in YYYY-MM-DD format
    
    """
    return datetime.datetime.now().strftime("%Y-%m-%d")