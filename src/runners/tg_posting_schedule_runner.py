import schedule
from constants import USED_PARSERS
import time
from src import db_client
from src import tg_bot
from datetime import datetime


def make_post_telegram():
    print(f'Постинг в телеграмм: {datetime.now()}')
    parser_names = list(map(lambda el: el.get_parser_name(), USED_PARSERS))
    posts = db_client.choise(parser_names)

    for post in posts:
        post_mess = f'{post[3]}, '  #title
        if post[2] != 0:
            post_mess += f'Цена: {post[2]} BYN, '  #price
        else:
            post_mess += 'Цена: не указана, '
        post_mess += f'Дата: {post[5]}, '  #date
        post_mess += f'Район: {post[7]}, '  #area
        post_mess += f" ".join(list(map(lambda el: el, post[6].split('{}')[:6])))  #photo_link
        tg_bot.send_post(post_mess)
        time.sleep(1)
    db_client.update_is_posted(list(map(lambda el: el[7], posts)))


schedule.every(6).minutes.do(make_post_telegram())


while True:
    schedule.run_pending()
    time.sleep(1)
