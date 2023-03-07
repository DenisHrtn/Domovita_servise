from abc import ABC, abstractmethod
from src import db_client


class ParserStandart(ABC):

    @abstractmethod
    def get_parser_name(self):
        return 'unnamed_parser'

    @abstractmethod
    def get_all_last_flats_links(self, page_from=1, page_to=3):
        return []

    @abstractmethod
    def enrich_links(self, links: list):
        return []

    @staticmethod
    def save_flats(flats):
        for counter, flat in enumerate(flats):
            print(f'Загружено в БД {counter} из {len(flats)}')
            db_client.insert_flat(flat)

    def update_with_last_flats(self, page_from=1, page_to=3):
        links = self.get_all_last_flats_links(page_from, page_to)
        flats = self.enrich_links(links)
        self.save_flats(flats)