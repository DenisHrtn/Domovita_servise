import schedule
from constants import USED_PARSERS
import threading
import time

PARSE_EVERY = 5

def parse_all():
    for parser in USED_PARSERS:
        thread = threading.Thread(target=parser.update_with_last_flats())
        thread.start()


schedule.every(PARSE_EVERY).minutes.do(parse_all())


while True:
    schedule.run_pending()
    time.sleep(1)