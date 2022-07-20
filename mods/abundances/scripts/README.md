# trident_mods
in progress modifications to Trident

A Pipeline designed to generate SALSA absorber catalogs from Trident for the purpose of quantifying uncertainties inherent to synthetic obsrvations. 

# Scripts
* sal_the_snek.py - uses SALSA to generate and save lightray objects and absorber catalogs to a given directory. Accepts a txt or csv file with abundance patterns different from solar abundances. If none are given, the saved data will be from that of solar abundances. The user can specify the number of lightray objects to be generated, the path to the directory where the data and rays will be stored, the path to an optional abundance file, and the path to the halo where the lightray objects will "pass through". This file can be run directly from the command line or though a bash script like sal_bash.txt
* sal_bash.txt - generally used for testing sal_the_snek.py functionality
* sal_analysis.py - uses the same ion list that is passed to SALSA and Trident, and writes the names of all the files containing this ion in the filename to a temporary .txt file. This temp file is passed to plot_clumps.py 
* plot_clumps.py - reads each .txt file from the temp file that sal_analysis.txt creates into a pandas dataframe. Then loops through each LightRay integer value and masks the dataframe to only contain data from that LightRay number. Produces a plot handy for combining interval chunks  
* make_hist.py - an example of two ways a histogram to analyze column densities can be produced. Uses the plot generated in plot_clumps.py
* dinkw_abundances.sb - an example of a job submission to the hpcc, the line starting with "python" can serve as an example of how to use sal_the_snek.py
* id_clumps_test.py - categorize clumps into different categories depending on how they compare to the rest of the clumps based on the data tables output from sal_the_snake.py
* make_hist_new.py - creates histograms based on the categories in id_clumps_test.py
* clump_stats.py - takes data from is_clumps_text and outputs statistics data tables
* sal_the_super_snek.py - combines sal_the_snek.py, id_clumps_test.py, and clump_stats.py into one pipeline
* make_interesting_plots.py - makes all the plots I was asked to make with the data from sal_the_super_snek.py

# Command Line Arguments for Sal the Super Snek
* --ds: Path where rays and output data will be stored. If other directories for data, stats, and rays are there, the program will make them using Python's os module
* --nrays: The number of lightray objects to be generated
* --abun: Path to abundance file
* --halo_dir: Path to halo data.
* --pat: Desired halo pattern file ID
* --rshift: Redshift file IDs

# Notes for the user
* Many of these scripts make use of default filepaths that are specific to me -- they will need to be modified to fit the user!
* Make sure the abundance file passed does not have any unnecessary characters (i.e. characters otherr than the element's name and the value associated with it) as this will confuse Trident and result in a runtime error.
* SALSA requires a "center_list" that is the center of the galaxy around which the halo resides. As of right now, this list is a default value in the program and, intuitively, this center_list will need to be changed if a different halo is used. 
* If passing abundance patterns to the program, the user will see the print statement, "Buckle up bc we're about to get wRIGGITY WRIGGITY WRECKED SON". This is intentional; it's how the user will know that Trident is using the abundances that were passed. 
