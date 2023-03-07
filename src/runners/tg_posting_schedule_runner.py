import schedule
from constants import USED_PARSERS
import time
from src import db_client
from src import tg_bot

PARSE_EVERY = 2

def make_post_telegram():
    parser_names = list(map(lambda el: el.get_parser_names(), USED_PARSERS))
    posts = db_client.choise(parser_names)
    for post in posts:
        post_mess = f'<b>Цена:</b> {post[2]} BYN/n'
        post_mess += f'<b>Описание:</b> {post[4]}/n/n'
        post_mess += '/n'.join(list(map(lambda el: el, post[6].split(',')[:6])))
        tg_bot.send_post(post_mess)
        time.sleep(1)
    db_client.update_is_posted(list(map(lambda el: el, posts[7])))

schedule.every(PARSE_EVERY).seconds.do(make_post_telegram())


while True:
    schedule.run_pending()
    time.sleep(1)