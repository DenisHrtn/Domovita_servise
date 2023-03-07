import schedule
from constants import USED_PARSERS
import threading
import time
from datetime import datetime


def parse_all():
    print(f'Парсер стартовал: {datetime.now()}')
    for parser in USED_PARSERS:
        thread = threading.Thread(target=parser.update_with_last_flats())
        thread.start()


schedule.every(5).minutes.do(parse_all())


while True:
    schedule.run_pending()
    time.sleep(1)