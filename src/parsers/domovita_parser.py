import requests
from bs4 import BeautifulSoup
from src.data import Flat
import re
from src.parsers.parser_standart import ParserStandart


class DomovitaParser(ParserStandart):

    def get_parser_name(self):
        return 'domovita'

    def get_all_last_flats_links(self, page_from=1, page_to=9):
        flat_links = []
        while page_from < page_to:
            resp = requests.get(f'https://domovita.by/minsk/flats/sale/?page={page_from}')
            html = BeautifulSoup(resp.content, 'html.parser')
            for a in html.find_all('a', href=True, class_='found_item p-0 clearfix d_flex OFlatsSale'):
                flat_links.append(a['href'])
                page_from += 1
        filter_links = list(filter(lambda el: 'flats' in el, flat_links))
        return filter_links

    def enrich_links(self, links):
        flats = []
        for counter, link in enumerate(links):
            resp = requests.get(link)
            html = BeautifulSoup(resp.content, 'html.parser')
            title = html.find('h1', class_='').text.strip()
            price = html.find(attrs={'data-js': 'show-tooltip'}).text
            if len(price) < 15:
                price = (re.sub('[^0-9]', '', price))
            else:
                price = 0
            description = html.find('div', class_='seo-text_content-h')
            if description is not None:
                description = description.text.strip()
            else:
                description = None
            date = html.find('span', class_='publication-info__item publication-info__publication-date').text.strip()
            area = html.find('span', class_='object-head__additional-info-item').text.strip()
            try:
                square = set()
                square_div = html.find_all('div', class_='object-head__additional-info')
                for square_span in square_div:
                    square_1 = square_span.findAllNext('span')
                    ready_square = square_1[1].text.strip()
                    square.add(ready_square)
                square = list(square)
            except Exception as e:
                square = []
            city = html.find(attrs={'id': 'city'}).text.strip()
            rooms = str(html.find(attrs={'title': '2-комнатные квартиры'}))
            micro = str(html.find('a', attrs={'href': 'https://domovita.by/minsk/kvartiru-lebyazhij/sale'}))
            try:
                images = set()
                image_div = html.find_all('div', {'class': 'pos-r'})
                for img_div in image_div:
                    img = img_div.findAll('img')
                    ready_images = img[1]['src']
                    images.add(ready_images)
                images = list(images)
                print()
            except Exception as e:
                images = []
            flats.append(Flat(
                link=link,
                title=title,
                price=price,
                description=description,
                date=date,
                area=area,
                square=square,
                city=city,
                rooms=rooms,
                micro=micro,
                reference=self.get_parser_name(),
                images=images
                ))
            print(f'Обработано {counter} из {len(links)}')
            print()
        return flats


DomovitaParser().update_with_last_flats()