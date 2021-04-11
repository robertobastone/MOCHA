import matplotlib.pyplot as plt # plotting
import matplotlib.gridspec as gridspec # for multiple subplots
import matplotlib.patches as mpatches #
import numpy as np # convert deg to radians and viceversa
import mocha_constellations as constellations
import mocha_plottersettings as listsettings

class mocha:

    def __init__(self):
        print("Initializing MOCHA...")

    def main(self):
        try:
            ### generating list of constellation-type objects
            list_constellations = constellations.loadData().listConstellations

            ### generating mocha_plottersettings object with plot settings
            settings = listsettings.getPlotSetting()

            ### create a figure 3x3
            fig = plt.figure(figsize=(settings.figsize_x,settings.figsize_y))
            spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
            fig.suptitle('Northern and Southern Constellations (Galactic frame)')

            ### PLOTTING CONSTELLATIONS IN GALACIC FRAME
            ax_galaxy = fig.add_subplot(spec[0:2, :], projection=settings.projectionHammer)
            ax_galaxy.grid(True)
            ax_galaxy.set_title('Galactic frame')
            ax_galaxy.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            ax_galaxy.set_ylabel(r'Galactic longitude $\mathrm{[\degree]}$')

            # drawing zoomed regions
            zoomedRegion1 = mpatches.Rectangle((np.radians(settings.zoom_1_x[0]), np.radians(settings.zoom_1_y[0])), np.radians(settings.zoom_1_width), np.radians(settings.zoom_1_height), linewidth=1, edgecolor='r', facecolor='none', zorder = settings.zoomedregionZorder)
            #zoomedRegion2 = mpatches.Rectangle((np.radians(settings.zoom_2_x[0]), np.radians(settings.zoom_2_y[0])), np.radians(settings.zoom_2_width), np.radians(settings.zoom_2_height), linewidth=1, edgecolor='r', facecolor='none', zorder = settings.zoomedregionZorder)
            zoomedRegion3 = mpatches.Rectangle((np.radians(settings.zoom_3_x[0]), np.radians(settings.zoom_3_y[0])), np.radians(settings.zoom_3_width), np.radians(settings.zoom_3_height), linewidth=1, edgecolor='r', facecolor='none', zorder = settings.zoomedregionZorder)
            ax_galaxy.add_patch(zoomedRegion1)
            #ax_galaxy.add_patch(zoomedRegion2)
            ax_galaxy.add_patch(zoomedRegion3)

            ### FIRST ZOOMED REGION
            ax_zoom1 = fig.add_subplot(spec[2, 0])
            ax_zoom1.grid(True)
            ax_zoom1.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            ax_zoom1.set_ylabel(r'Galactic longitude $\mathrm{[\degree]}$')
            ax_zoom1.set_title('Zoomed region ' + str(settings.zoom_1_width) + r'$\mathrm{\degree}$x' + str(settings.zoom_1_height) + r'$\mathrm{\degree}$')
            ax_zoom1.set_xlim(settings.zoom_1_x[0],settings.zoom_1_x[1])
            ax_zoom1.set_ylim(settings.zoom_1_y[0],settings.zoom_1_y[1])

            ### SECOND ZOOMED REGION --- NOW IT IS A LAMBERT PROJECTION OF AX GALAXY
            ax_zoom2 = fig.add_subplot(spec[2, 1], projection=settings.projectionLambert)
            ax_zoom2.grid(True)
            ax_zoom2.locator_params(axis='x', nbins=settings.bins_2_x)
            ax_zoom2.set_title('Ecliptic Constellations (galactic frame)')
            ax_zoom2.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            #ax_zoom2.set_xlim(settings.zoom_2_x[0],settings.zoom_2_x[1])
            #ax_zoom2.set_ylim(settings.zoom_2_y[0],settings.zoom_2_y[1])

            ### THIRD ZOOMED REGION
            ax_zoom3 = fig.add_subplot(spec[2, 2])
            ax_zoom3.grid(True)
            ax_zoom3.set_xlabel(r'Galactic latitude $\mathrm{[\degree]}$')
            ax_zoom3.set_title('Zoomed region ' + str(settings.zoom_3_width) + r'$\mathrm{\degree}$x' + str(settings.zoom_3_height) + r'$\mathrm{\degree}$')
            ax_zoom3.set_xlim(settings.zoom_3_x[0],settings.zoom_3_x[1])
            ax_zoom3.set_ylim(settings.zoom_3_y[0],settings.zoom_3_y[1])

            ### PLOTTING
            for constellation in list_constellations:
                print('Plotting... ' + str(constellation.name))
                for star in constellation.list_star:
                    x = star.galacticLatitude.value
                    y = star.galacticLongitude.value
                    ax_galaxy.scatter(np.radians(x), np.radians(y), color=settings.starColor, marker=settings.starMarker, s = settings.starSize, zorder = settings.starZorder)
                    ax_zoom1.scatter(x,y, color=settings.starColor, marker=settings.starMarker, s = settings.starSize, zorder = settings.starZorder)
                    if constellation.name in settings.eclipticConstellations:
                        ax_zoom2.scatter(np.radians(x),np.radians(y), color=settings.starColor, marker=settings.starMarker, s = settings.starSize, zorder = settings.starZorder)
                    ax_zoom3.scatter(x,y, color=settings.starColor, marker=settings.starMarker, s = settings.starSize, zorder = settings.starZorder)
                    bonds = star.bonds.split(';')
                    for bond in bonds:
                        for astrum in constellation.list_star:
                            if astrum.mochaId == bond:
                                x2 = astrum.galacticLatitude.value
                                y2 = astrum.galacticLongitude.value
                                ax_galaxy.plot( (np.radians(x), np.radians(x2)),
                                                (np.radians(y), np.radians(y2)), color = settings.constellationColor, linewidth = settings.constellationSize, zorder=settings.constellationZorder)
                                ax_zoom1.plot((x,x2),(y,y2), color = settings.constellationColor, linewidth = settings.constellationSize, zorder=settings.constellationZorder)
                                if constellation.name in settings.eclipticConstellations:
                                    ax_zoom2.plot((np.radians(x), np.radians(x2)),(np.radians(y), np.radians(y2)), color = settings.constellationColor, linewidth = settings.constellationSize, zorder=settings.constellationZorder)
                                ax_zoom3.plot((x,x2),(y,y2), color = settings.constellationColor, linewidth = settings.constellationSize, zorder=settings.constellationZorder)
            ### SAVE PLOT
            plt.savefig('mocha.png', dpi=400)
        except Exception as e:
            print(str(e))
