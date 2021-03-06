#!/usr/bin/env python3

# Import System Libraries
import traceback
import logging

# Import External Libraries
from bs4 import BeautifulSoup

# Import Custom Data Structure
from torrentscraper.datastruct.rawdata_instance import RAWDataInstance

# Import Custom Exceptions
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperParseError
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperContentError
from torrentscraper.webscrapers.exceptions.webscraper_error import WebScraperProxyListError

# Import Custom Constants
from lib.fileflags import FileFlags as fflags

class TorrentFunkScraper(object):
    def __init__(self, logger):
        '''

        :param logger:
        '''
        self.name = self.__class__.__name__

        # CustomLogger
        self.logger = logger

        # Scraper Configuration Parameters
        self.query_type = False
        self.batch_style = False
        self.cloudflare_cookie = False
        self.thread_defense_bypass_cookie = False

        # Sleep Limit, for connections to the web source
        self.safe_sleep_time = [1.0, 1.5]

        # Supported FileFlags
        self.supported_searchs = [fflags.FILM_DIRECTORY_FLAG, fflags.SHOW_DIRECTORY_FLAG, fflags.ANIME_DIRECTORY_FLAG]

        # ProxyList Parameters
        self.proxy_list = ['https://torrentfunk.unblocked.mx','https://www.torrentfunk.com']
        self._proxy_list_pos = 0
        self._proxy_list_length = len(self.proxy_list)
        self.main_page = self.proxy_list[self._proxy_list_pos]

        # Uri Composition Parameters
        self.default_params = {}
        self.default_search = '/all/torrents/'
        self.default_tail = '.html'

        # Hop Definitions
        self.batch_hops = []
        self.hops = [self.get_magnet_link]

    def update_main_page(self):
        '''

        :return:
        '''
        try:
            value = self._proxy_list_pos
            if self._proxy_list_length > self._proxy_list_pos:
                value += 1

            self._proxy_list_pos = value
            self.main_page = self.proxy_list[self._proxy_list_pos]
        except IndexError as err:
            raise WebScraperProxyListError(self.name, err, traceback.format_exc())

    def get_raw_data(self, content=None):
        '''

        :param content:
        :return:
        '''
        raw_data = RAWDataInstance()
        soup = BeautifulSoup(content, 'html.parser')

        try:
            # Retrieving individual values from the search result
            ttable = soup.findAll('table', {'class':'tmain'})
            if ttable is not []:
                try:
                    self.logger.info('{0} Retrieving Raw Values from Search Result Response:'.format(self.name))
                    for items in ttable:
                        tbody = items.findAll('tr')
                        for tr in tbody[1:]:
                            seed = (tr.findAll('td'))[3].text
                            if seed == '0':
                                seed = '1'

                            leech = (tr.findAll('td'))[4].text
                            if leech == '0':
                                leech = '1'

                            # Converting GB to MB, to Easily Manage The Pandas Structure
                            size = (tr.findAll('td'))[2].text
                            if 'MB' in size:
                                size = float(size[:-2])
                            elif 'GB' in size:
                                size = float(size[:-2]) * 1000

                            magnet_link = (tr.findAll('a'))[0]['href']

                            # Patch to Avoid Getting False Torrents
                            if int(seed) < 1500:
                                raw_data.add_new_row(size, seed, leech, magnet_link)
                                self.logger.debug('{0} New Entry Raw Values: {1:7} {2:>4}/{3:4} {4}'.format(
                                    self.name, str(int(size)), str(seed), str(leech), magnet_link))
                except Exception as err:
                    raise WebScraperParseError(self.name, 'ParseError: unable to retrieve values: {0}'.format(err),
                                               traceback.format_exc())
        except Exception as err:
            raise WebScraperContentError(self.name, 'ContentError: unable to retrieve values {0}'.format(err),
                                         traceback.format_exc())
        return raw_data

    def get_magnet_link(self, content, *args):
        ''''''
        soup = BeautifulSoup(content, 'html.parser')
        try:
            content = (soup.findAll('div',{'class':'content'}))
            if content is not []:
                try:
                    magnet = content[2].findAll('a')[1]['href']
                    return magnet
                except Exception as err:
                    raise WebScraperParseError(self.name, 'ParseError: unable to retrieve values: {0}'.format(err),
                                               traceback.format_exc())
        except Exception as err:
            raise WebScraperContentError(self.name, 'ContentError: unable to retrieve values {0}'.format(err),
                                         traceback.format_exc())
