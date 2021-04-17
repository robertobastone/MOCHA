######################### LIBRARIES #########################

######################### CODE #########################

class getPlotSetting:

    def __init__(self):
        ## general plotting settings
        self.figsize_x = 13
        self.figsize_y = 10
        self.projectionHammer = 'hammer'
        self.projectionLambert = 'lambert'
        self.sizeOfFont = 8
        self.ratiooffset = 80
        self.zoomedregionZorder=200
        # ax_scatter settings
        self.starZorder = 100
        self.starMarker = '*'
        self.starColor = 'darkgoldenrod'
        self.starSize = 3
        # ax_plot settings
        self.constellationZorder = 50
        self.constellationColor = 'cornflowerblue'
        self.constellationSize = 1
        # zoom 1 settings
        self.zoom_1_x = [-170,-140]
        self.zoom_1_width = self.zoom_1_x[1] - self.zoom_1_x[0]
        self.zoom_1_y = [0,20]
        self.zoom_1_height = self.zoom_1_y[1] - self.zoom_1_y[0]
        self.zoom_1_offsetx = self.zoom_1_width/self.ratiooffset
        # zoom 2 settings --- now lambert projection of ecliptic constellations
        self.eclipticConstellations = ['Aries', 'Taurus', 'Gemini',
                                       'Cancer', 'Leo', 'Virgo',
                                       'Libra', 'Scorpio', 'Ophiuchus', 'Sagittarius',
                                       'Capricorn', 'Aquarius', 'Pisces']
        self.bins_2_x = 9
        '''
        self.zoom_2_x = [5,20]
        self.zoom_2_width = self.zoom_2_x[1] - self.zoom_2_x[0]
        self.zoom_2_y = [-8,4]
        self.zoom_2_height = self.zoom_2_y[1] - self.zoom_2_y[0]
        self.zoom_2_offsetx = self.zoom_2_width/self.ratiooffset
        '''
        # zoom 3 settings
        self.zoom_3_x = [20,70]
        self.zoom_3_width = self.zoom_3_x[1] - self.zoom_3_x[0]
        self.zoom_3_y = [-20,20]
        self.zoom_3_height = self.zoom_3_y[1] - self.zoom_3_y[0]
        self.zoom_3_offsetx = self.zoom_3_width/self.ratiooffset
