import traceback
import schedule
from constants import USED_PARSERS
import time
from src import db_client
from src import tg_bot
import logging
import src.loger_db as loger
from src.sentry import sentry


def make_post_telegram(log):
    try:
        parser_names = list(map(lambda el: el.get_parser_name(), USED_PARSERS))
        posts = db_client.choise(parser_names)

        for post in posts:
            logging.info(f'Телеграмм-постер обрабатывает: ({log})')
            log = post
            # title
            post_mess = f'{post[3]}, '
            if post[2] != 0:
                # price
                post_mess += f'Цена: {post[2]} BYN, '
            else:
                # if price is none
                post_mess += 'Цена: не указана, '
            # date
            post_mess += f'Дата: {post[5]}, '
            # area
            post_mess += f'Район: {post[7]}, '
            # photo_link
            post_mess += f" ".join(list(map(lambda el: el, post[6].split('{}')[:6])))
            tg_bot.send_post(post_mess)
            logging.info(f'Телеграмм-постер сделал пост:({post})')
            time.sleep(1)
        db_client.update_is_posted(list(map(lambda el: el[7], posts)))
    except Exception as e:
        logging.error(f'При работе телеграмм-постера произошла ошибка: {traceback.format_exc()}')


schedule.every(6).minutes.do(make_post_telegram(log=logging.info(f'Телеграмм-постер начал работу')))


while True:
    schedule.run_pending()
    time.sleep(1)