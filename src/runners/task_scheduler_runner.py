import traceback
import schedule
from constants import USED_PARSERS
import threading
import time
import logging
import src.loger_db as loger
from src.sentry import sentry


def parse_all(log):
    try:
        for parser in USED_PARSERS:
            log = parser
            logging.info(f'Парсер стартовал({log})')
            logging.info(f'Парсер завершил работу({log})')
            thread = threading.Thread(target=parser.update_with_last_flats())
            thread.start()
    except Exception as e:
        logging.error(f'При работе парсера произошла ошибка: {traceback.format_exc()}')


try:
    schedule.every(5).minutes.do(parse_all(log=logging.info('Парсер начал работать')))
except Exception as e:
    logging.error(f'При работе парсера произошла ошибка: {traceback.format_exc()}')

while True:
    schedule.run_pending()
    time.sleep(1)
