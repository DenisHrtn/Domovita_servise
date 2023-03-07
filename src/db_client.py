import psycopg2

DBNAME = 'postgres'
USER = 'postgres'
PASSWORD = '95233574'
HOST = 'localhost'

FLATS_TABLE = 'flats'

def create_flats_table():
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            CREATE TABLE IF NOT EXISTS flats(
                id serial PRIMARY KEY,
                link CHARACTER VARYING(300) UNIQUE NOT NULL,
                reference CHARACTER VARYING(30),
                price INTEGER,
                title CHARACTER VARYING(300),
                description CHARACTER VARYING,
                date CHARACTER VARYING(30),
                area CHARACTER VARYING(50),
                square INTEGER,
                city CHARACTER VARYING(150),
                rooms CHARACTER VARYING(150),
                micro CHARACTER VARYING(150)
                )''')


def insert_flat(flat):
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            INSERT INTO flats (link, reference, price, title, description, date, area, square, city, rooms, micro, photo_links) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (link) DO UPDATE
            SET
            link = EXCLUDED.link,
            reference = EXCLUDED.reference,
            price = EXCLUDED.price,
            title = EXCLUDED.title,
            description = EXCLUDED.description,
            date = EXCLUDED.date,
            area = EXCLUDED.area,
            square = EXCLUDED.square,
            city = EXCLUDED.city,
            rooms = EXCLUDED.rooms,
            micro = EXCLUDED.micro
            ''',  (flat.link, flat.reference, flat.price, flat.title, flat.description, flat.date, flat.area, flat.square, flat.city, flat.rooms, flat.micro, flat.images))

def choise(parser_types):
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
                    SELECT link, reference, price, title, description, date, photo_links, id FROM flats
                    WHERE (is_tg_posted = false or is_tg_posted IS NULL)  
                    and reference IN %(parser_types)s
            ''',
                         {'parser_types': tuple(parser_types)}
                         )
            curs.fetchall()

def update_is_posted(ids):
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
                UPDATE flat SET
                is_tg_posted = True 
                WHERE id ANY(%s)
            ''',
                         {ids, }
                         )

create_flats_table()