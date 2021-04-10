import matplotlib.pyplot as plt # plotting
import matplotlib.gridspec as gridspec # for multiple subplots
import matplotlib.patches as mpatches #
import numpy as np # convert deg to radians and viceversa
import mocha_constellations as constellations

class mocha:
    def __init__(self):
        print("Initializing MOCHA...")
    def main(self):
        try:

            list_constellations = constellations.loadData().listConstellations
            ### create a figure 3x3
            fig = plt.figure(figsize=(13,10))
            spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
            fig.suptitle('Northern and Southern Constellations (Galactic frame)')
            ### PLOTTING MESSIER OBJECTS IN GALACIC FRAME
            ax_galaxy = fig.add_subplot(spec[0:2, :], projection='hammer')
            ax_galaxy.grid(True)
            ax_galaxy.set_title('Galactic frame')
            ax_galaxy.locator_params(axis='x', nbins=22)
            ax_galaxy.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            ax_galaxy.set_ylabel(r'Galactic longitude $\mathrm{[\degree]}$')

            # drawing zoomed regions
            '''
            zoomedRegion1 = mpatches.Rectangle((np.radians(self.zoom_1_x[0]), np.radians(self.zoom_1_y[0])), np.radians(self.zoom_1_width), np.radians(self.zoom_1_height), linewidth=1, edgecolor='r', facecolor='none', zorder = self.zorder)
            zoomedRegion2 = mpatches.Rectangle((np.radians(self.zoom_2_x[0]), np.radians(self.zoom_2_y[0])), np.radians(self.zoom_2_width), np.radians(self.zoom_2_height), linewidth=1, edgecolor='r', facecolor='none', zorder = self.zorder)
            ax_galaxy.add_patch(zoomedRegion1)
            ax_galaxy.add_patch(zoomedRegion2)
            '''

            ### PLOTTING FIRST ZOOMED REGION
            ax_zoom1 = fig.add_subplot(spec[2, 0])
            ax_zoom1.grid(True)
            ax_zoom1.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            ax_zoom1.set_ylabel(r'Galactic longitude $\mathrm{[\degree]}$')
            '''
            ax_zoom1.set_title('Zoomed region ' + str(self.zoom_1_width) + r'$\mathrm{\degree}$x' + str(self.zoom_1_height) + r'$\mathrm{\degree}$')
            ax_zoom1.set_xlim(self.zoom_1_x[0],self.zoom_1_x[1])

            ax_zoom1.set_ylim(self.zoom_1_y[0],self.zoom_1_y[1])
            '''

            ### PLOTTING SECOND ZOOMED REGION
            ax_zoom2 = fig.add_subplot(spec[2, 1])
            ax_zoom2.grid(True)
            ax_zoom2.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')

            '''
            ax_zoom2.set_title('Zoomed region ' + str(self.zoom_2_width) + r'$\mathrm{\degree}$x' + str(self.zoom_2_height) + r'$\mathrm{\degree}$')
            ax_zoom2.set_xlim(self.zoom_2_x[0],self.zoom_2_x[1])
            ax_zoom2.set_ylim(self.zoom_2_y[0],self.zoom_2_y[1])
            '''

            for constellation in list_constellations:
                print('---------')
                for star in constellation.list_star:
                    print(constellation.name)
                    print(star.name)
                    print(star.galacticLatitude)
                    print(star.galacticLongitude)
                    x = star.galacticLatitude.value
                    y = star.galacticLongitude.value
                    print(x)
                    print(y)
                    ax_galaxy.scatter(np.radians(x), np.radians(y), color='yellow', marker='*', s = 1)
                    ax_zoom1.scatter(x,y, color='yellow', marker='*')
                    bonds = star.bonds.split(';')
                    for bond in bonds:
                        for astrum in constellation.list_star:
                            if astrum.mochaId == bond:
                                x2 = astrum.galacticLatitude.value
                                y2 = astrum.galacticLongitude.value
                                ax_galaxy.plot( (np.radians(x), np.radians(x2)),
                                                (np.radians(y), np.radians(y2)), color = 'blue' )
                                ax_zoom1.plot((x,x2),(y,y2), color = 'blue')
                '''
                x, y, mark, color = self.getMessierObjectDataForPlotting(dictionary, mo)
                ax_galaxy.scatter(np.radians(x), np.radians(y), marker = mark, color= color, s=self.gal_sizeOfMarkers, linewidth=1, zorder = self.zorder)
                ax_zoom1.scatter(x,y, marker = mark, color= color, s=self.sizeOfMarkers, linewidth=1, zorder = self.zorder)
                ax_zoom1.annotate(str(mo.name), (x+self.zoom_1_offsetx,y), fontsize = self.sizeOfFont)
                ax_zoom2.scatter(x,y, marker = mark, color= color, s=self.sizeOfMarkers, linewidth=1, zorder = self.zorder)
                ax_zoom2.annotate(str(mo.name), (x+self.zoom_2_offsetx,y), fontsize = self.sizeOfFont)
                #print(str(mo.name)  +  str(mark) + str(color) )
                '''
            ax_zoom3 = fig.add_subplot(spec[2, 2])
            ax_zoom3.grid(True)
            ax_zoom3.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')

            plt.savefig('mocha.png', dpi=400)
        except Exception as e:
            print(str(e))
