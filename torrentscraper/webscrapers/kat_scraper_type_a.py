#!/usr/bin/env python3

# Import System Libraries
import traceback

# Import External Libraries
from bs4 import BeautifulSoup

# Import Custom Data Structure
from torrentscraper.datastruct.rawdata_instance import RAWDataInstance

# Import Custom Exceptions
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperProxyListError
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperParseError
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperContentError

# Constants
from lib.fileflags import FileFlags as fflags

FILM_FLAG = fflags.FILM_DIRECTORY_FLAG
SHOW_FLAG = fflags.SHOW_DIRECTORY_FLAG
ANIME_FLAG = fflags.ANIME_DIRECTORY_FLAG

class KatScrapperTypeA():
    def __init__(self, logger):
        self.name = self.__class__.__name__
        self.logger = logger
        self.proxy_list = ['https://kickass.cd']
        self._proxy_list_length = len(self.proxy_list)
        self._proxy_list_pos = 0
        self.cloudflare_cookie = False
        self.query_type = True
        self.disable_quality = False
        self.thread_defense_bypass_cookie = False
        self.torrent_file = False
        self.magnet_link = False

        self.main_page = self.proxy_list[self._proxy_list_pos]
        self.default_search = '/search.php'
        self.default_tail = ''
        self.default_params = {}
        self.supported_searchs = [FILM_FLAG, SHOW_FLAG]

    def update_main_page(self):
        try:
            value = self._proxy_list_pos
            if self._proxy_list_length > self._proxy_list_pos:
                value += 1

            self._proxy_list_pos = value
            self.main_page = self.proxy_list[self._proxy_list_pos]
        except IndexError as err:
            raise WebScraperProxyListError(self.name, err, traceback.format_exc())

    def get_raw_data(self, content=None):
        raw_data = RAWDataInstance()
        soup = BeautifulSoup (content, 'html.parser')

        try:
            ttable = soup.findAll('tr', {'class':'odd'})
            # Retrieving Individual Raw Values From Search Result
            if ttable != []:
                self.logger.info('{0} Retrieving Raw Values from Search Result Response:'.format(self.name))
                for items in ttable:
                    _pos = len(raw_data.magnet_list)

                    seed = (soup.findAll('td', {'class': 'green center'}))[ _pos].text
                    if seed == '0':
                        seed = '1'

                    leech = (soup.findAll('td', {'class': 'red lasttd center'}))[ _pos].text
                    if leech == '0':
                        leech = '1'

                    size = (items.findAll('td', {'class': 'nobr center'}))[0].text
                    # Converting GB to MB, to Easily Manage The Pandas Structure
                    if 'MiB' in size:
                        size = size.replace('MiB', 'MB')
                        size = float(size[:-3])
                    elif 'GiB' in size:
                        size = size.replace('GiB', 'GB')
                        size = float(size[:-3]) * 1000

                    magnet_link = (items.findAll('a', {'title': 'Torrent magnet link'}))[0]['href']

                    raw_data.add_magnet(magnet_link)
                    raw_data.add_size(int(size))
                    raw_data.add_seed(int(seed))
                    raw_data.add_leech(int(leech))

                    self.logger.debug('{0} New Entry Raw Values: {1:7} {2:>4}/{3:4} {4}'.format(self.name,
                                                                                                  str(int(size)),
                                                                                                  str(seed),
                                                                                                  str(leech),
                                                                                                  magnet_link))
            else:
                raise WebScraperContentError(self.name, 'ContentError: unable to retrieve values', traceback.format_exc())
        # TODO corregir esto para que no capture
        except WebScraperContentError as err:
            raise WebScraperContentError(err.name, err.err, err.trace)
        except Exception as err:
            raise WebScraperParseError(self.name, err, traceback.format_exc())
        return raw_data

    def magnet_link_scrapper(self, content):
        return
