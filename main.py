#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from torrent_scraper_interface import run_interface
from description_downloader import DescriptionDownloader
from lib.fileflags import FileFlags as fflags

FILM_DIRECTORY_FLAG = '9'

def main():
    run_interface()
    # desc = DescriptionDownloader()
    # info = desc.get_info(fflags.FILM_DIRECTORY_FLAG, 'Kong: Skull Island')
    # # print(info)

if __name__ == '__main__':
    main()

# TODO Añadir Internacionalizacion
# TODO Corregir el bug, que genera WebscraperContentError y ErrorProxy al no permitir finalizar el proceoso.
# TODO Añadir cache a la descripcion
# TODO Añadir boton de clear cache en el config menu, en general
# TODO Funcion de Save de QbitConfigDataPanel
# TODO Propagar Theme por los objetos, añadirlo al menu de configuración general, y limpiar el codigo

    # cv = CoverDownloader()
    # ws = WebSearchInstance(title='Marvel Avengers', year='2012', quality='1080p', search_type='FILM')
    # cv.download(ws)

    # ws = WebSearchInstance(title='Avengers', year='2012', quality='1080p', search_type='FILM')
    # ts = TorrentScraper()
    # ts.scrap(ws)

    # tvdb = TVDbShowExtension()
    # print(tvdb.get_year('Scrubs'))
    # print(tvdb.get_runtime('Scrubs'))
    # print(tvdb.get_description('Scrubs'))

    # from Pymoe import Anilist
    # instance = Anilist()
    # result = instance.search.anime("Fullmetal Alchemist: Brotherhood")
    # print(result['data'])
    # # print(result['data']['Page']['averageScore'])
    # id = result['data']['Page']['media'][0]['id']
    #
    # result = instance.get.anime(5114)
    # print(result)
    # year = result['data']['Media']['startDate']['year']
    # episodes = result['data']['Media']['episodes']
    # description = result['data']['Media']['description']
    # rating = result['data']['Media']['averageScore']
    # print(year)
    # print(episodes)
    # print(description)
    # print(rating)
    #
    # print('staff', instance.get.staff(5114))
    #
    # import myanimelist.session
    # session = myanimelist.session.Session()
    # # Return an anime object corresponding to an ID of 1. IDs must be natural numbers.
    # data = session.anime(5114)
    # print(data)
    # for character in data.characters:
    #     print(character.name, '---', data.characters[character]['role'])