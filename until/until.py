from random import choice
import pytz
from datetime import datetime

def check_monet():
    return choice(["орел", "решка"])

def get_time():
    tz_time = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz_time)
    return current_time.strftime("%H:%M:%S")