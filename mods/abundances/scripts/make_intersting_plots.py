import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import pandas as pd
import numpy as np

halo_marker_dict = {'2392' : 'o', '4123' : 'x', '5016' : 'v', '5036' : '*', '8508' : 'D'} ##set which marker I want for each halo
halo_names_dict = {'2392'  :  'Hurricane' ,'2878'  :  'Cyclone' , '4123'  :  'Blizzard' , '5016'  :  'Squall' ,'5036'  :  'Maelstrom' , '8508'  :  'Tempest'} ##set FOGGIE names

def get_halo_names(num): ##get the FOGGIE name for each halo ID 
    if str(num) in halo_names_dict.keys():
        halo_name = halo_names_dict[str(num)]
    return halo_name


rs_lis = [2.0, 2.5] ##list of rs to analyze, true


ion_dict = {'C_II':'C4', 'C_IV':'C2', 'O_VI': 'C1'} ##dictionary of ions to colors

##set the legends to be the way I want them
legend_elements = [Line2D([0], [0], lw= 0, color = 'k', marker = 'o', label = 'Hurricane'), Line2D([0], [0],  lw= 0, color = 'k', marker = 'x', label = 'Cyclone'), Line2D([0], [0],  lw= 0, color = 'k', marker = 'v', label = 'Squall'), Line2D([0], [0], lw= 0, color = 'k', marker = '*', label = 'Maelstrom'), Line2D([0], [0], lw= 0, color = 'k', marker = 'D', label = 'Tempest'), Patch(fc = 'C4', label = 'C_II'), Patch(fc = 'C2', label = 'C_IV'), Patch(fc = 'C1', label = 'O_IV')]

for rs in rs_lis: ##we want one graph per redshift
    for halo in halo_marker_dict.keys(): ##all the halos
        name = get_halo_names(halo)
        for ion in ion_dict.keys(): ##all the ions
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):##exclude halos that don't work
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv') ##something to tell me the code is actually running
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                med_col_dens = ds["median_col_desnity"] ##plot the spread of the median vs the median col dens
                col_dens_spread = ds["mad_for_col_desnity"]
                plt.scatter(med_col_dens, col_dens_spread, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"MAD of Column Density vs Column Density, Redshift {rs}") 
    plt.legend(handles = legend_elements, ncol = 2)
    plt.xlabel("Median log(Column Density)")
    plt.ylabel("MAD of log(Column Density)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/mad_vs_med_z{rs}.png') ##make sure it saves to the right place with the right name
    plt.close() ##so the rest doesn't plot on top of this data
    ##a simmilar process is used for the rest of these plots, simply with different quantities
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                med_col_dens = ds["median_col_desnity"] ##density and median column density
                dens = ds["density"]
                plt.scatter(med_col_dens, dens, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Density vs Column Density, Redshift {rs}")
    plt.yscale('log') ##has to be plotted on a log scale
    plt.legend(handles = legend_elements, ncol = 2)
    plt.xlabel("Median log(Column Density)")
    plt.ylabel("log(Density)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/dens_vs_med_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                med_col_dens = ds["median_col_desnity"] ##temperature and median column density
                temp = ds["temperature"]
                plt.scatter(med_col_dens, temp, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Temperature vs Column Density, Redshift {rs}")
    plt.yscale('log') 
    plt.legend(handles = legend_elements, ncol = 2)
    plt.xlabel("Median log(Column Density)")
    plt.ylabel("log(Temperature)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/temp_vs_med_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                med_col_dens = ds["median_col_desnity"] ##distance from galaxy vs median col dens
                dist = ds["distance_from_galaxy"]
                plt.scatter(med_col_dens, dist, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Distance vs Column Density, Redshift {rs}")
    plt.legend(handles = legend_elements, ncol = 2)
    plt.xlabel("Median log(Column Density)")
    plt.ylabel("Distance from Galaxy")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/dist_vs_med_z{rs}.png')
    plt.close()

    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                col_dens_spread = ds["mad_for_col_desnity"] ##MAD of col dens vs density
                dens = ds["density"]
                plt.scatter(dens, col_dens_spread, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Density vs Spread of Column Density , Redshift {rs}")
    plt.xscale('log')
    plt.legend(handles = legend_elements, ncol = 2)
    plt.ylabel("MAD of Median log(Column Density)")
    plt.xlabel("log(Density)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/dens_vs_mad_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                col_dens_spread = ds["mad_for_col_desnity"] ##MAD of col dons vs temperature
                temp = ds["temperature"]
                plt.scatter(temp, col_dens_spread, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Temperature vs Spread of Column Density, Redshift {rs}")
    plt.xscale('log')
    plt.legend(handles = legend_elements, ncol = 2)
    plt.ylabel("MAD of Median log(Column Density)")
    plt.xlabel("log(Temperature)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/temp_vs_mad_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                col_dens_spread = ds["mad_for_col_desnity"] ##MAD of col dens vs distance from galaxy
                dist = ds["distance_from_galaxy"]
                plt.scatter(dist, col_dens_spread, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Distance vs Spread of Column Density, Redshift {rs}")
    plt.legend(handles = legend_elements, ncol = 2)
    plt.ylabel("MAD of Median log(Column Density)")
    plt.xlabel("Distance from Galaxy")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/dist_vs_mad_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                med_col_dens = ds["median_col_desnity"] ##median col dens vs frequency of clumps splitting or getting shorter
                num_spl_sho = ds["num_split_or_short"]
                plt.scatter(med_col_dens, num_spl_sho, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"Frequency of Split or Short Clumps vs Column Density, Redshift {rs}")
    plt.legend(handles = legend_elements, ncol = 2, markerscale = 0.75, fontsize = 'x-small')
    plt.xlabel("Median log(Column Density)")
    plt.ylabel("Number of Split or Short Clumps")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/freq_vs_med_z{rs}.png')
    plt.close()
    
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                elem_mad = ds["mad_of_element"] ##MAD of elemental abundance vs MAD of the col dens
                col_dens_spread = ds["mad_for_col_desnity"]
                plt.scatter(col_dens_spread, elem_mad, c = ion_dict[ion], marker = halo_marker_dict[halo])
      
    plt.title(f"MAD of Elemental Abundance vs MAD of Column Density, Redshift {rs}")
    plt.legend(handles = legend_elements, ncol = 2)
    plt.ylabel("MAD of Elemental Abundance")
    plt.xlabel("MAD of log(Column Density)")
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/mad_vs_elem_mad_z{rs}.png')
    plt.close()
    
    ##this one is different because it's a histogram and not a scatter plot
    diff_list = [] ##initalize list to be put into a histogram
    for halo in halo_marker_dict.keys():
        name = get_halo_names(halo)
        for ion in ion_dict.keys():
            if (halo == '2392' and rs == 2.5) or (halo == '5016' and rs == 2.5):
                continue
            else:
                print(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv')
                ds = pd.read_csv(f'/mnt/scratch/f0104093/cgm_abundance_variance/halo{halo}/redshift{rs}/stats/{halo}_z{rs}_{ion}_abun_all-model-families_all-clumps.csv', delim_whitespace = True)
                diff = ds["diff_from_solar_abun"] ##get the data from data tables
                for value in diff:
                    if value != 'NaN' and value != np.NaN: ##filter out the NaNs
                        diff_list.append(value) ##make the list of values
      
    plt.hist(diff_list) ##make the histogram
    plt.title(f"Diffrence between Solar Abundance and Median Column Density, Redshift {rs}") ##needs a better title but I can't think of one right now
    plt.ylabel("frequency")
    plt.xlabel("dex of the difference between Solar Abundance Column Density and Median Column Density") ##has to be in dex(order of magnitude) because of how sal the super snake works
    plt.savefig(f'/mnt/scratch/f0104093/cgm_abundance_variance/graphs/solar_diff_z{rs}.png')
    plt.close()
