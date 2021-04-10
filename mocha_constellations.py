######################### LIBRARIES #########################
import os # info about file
import sys # better management of the exceptions
import pandas as pd # open excel file
from termcolor import colored # customize ui
from pprint import pprint
import astropy.units as u # managing units of measure
from astropy.coordinates import SkyCoord # managing coordinate systems

dataLocation ='constellations.xlsx'

class loadData:

    def __init__(self):
        self.listConstellations = []
        try:
            print(colored("Loading data... ", 'blue'))
            self.listConstellations = self.getData()
        except Exception as e:
            print(colored(str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))

    def getData(self):
        try:
            workbook = pd.ExcelFile(dataLocation)
            listConstellations = []
            for worksheets in workbook.sheet_names:
                constellation_sheet = workbook.parse(worksheets)
                number_rows = constellation_sheet.shape[0]
                list_star = []
                for index in range(0,number_rows):
                    star = constellation_sheet.iloc[index]
                    astrum = generatingStar(star['Name'],
                                            star['MochaId'],
                                            star['RA'],
                                            star['Dec'],
                                            star['Bonds'],
                                            star['Constellation'])
                    list_star.append(astrum)
                constellation = generatingConstellation(worksheets,list_star)
                listConstellations.append(constellation)
            return listConstellations
        except Exception as e:
            print(colored("The following exception was catched:" + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))

######### defining wrapper class for Messier Objects
class Constellation(object):
    name = ""
    list_star = []

    def __init__(self, name, list_star):
        self.name = name
        self.list_star = list_star



class Star(object):
    name = ""
    mochaId = ""
    galacticLatitude = 0
    galacticLongitude = 0
    bonds = ""
    constellation = ""

    def __init__(self, name, mochaId, ra, dec, bonds, constellation):
        c = SkyCoord(str(ra) + ' ' + str(dec), unit=(u.hourangle, u.deg))
        self.name = name
        self.mochaId = mochaId
        self.galacticLatitude = c.galactic.l.wrap_at('180d') # from ra to gal_lat
        self.galacticLongitude = c.galactic.b # from dec to gal_long
        self.bonds = bonds
        self.constellation = constellation


def generatingConstellation(name, list_star):
    constellation = Constellation(name, list_star)
    return constellation

def generatingStar(name, mochaId, ra, dec, bonds, constellation):
    star = Star(name, mochaId, ra, dec, bonds, constellation)
    return star
