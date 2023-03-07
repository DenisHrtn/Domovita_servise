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
        post_mess = f'<b>Цена:</b> {post[2]} BYN'
        post_mess += f'<b>Дата:</b> {post[5]}'
        post_mess += '/n'.join(list(map(lambda el: el, post[6].split('{}')[:6])))
        tg_bot.send_post(post_mess)
        time.sleep(1)
    db_client.update_is_posted(list(map(lambda el: el[7], posts)))

schedule.every(6).minutes.do(make_post_telegram())


while True:
    schedule.run_pending()
    time.sleep(1)
