The Postanalyzer procedure is controlled by a single file which centralizes all 
the possible actions one can do on the data files.

-> go to "steer_datacards.py"

In that file, you will find all the parameters that are needed to run the code. 
The lines indicated with a "!", are the ones that are most commonly modified, and the others
for more subtle changes in the code. Be careful that changing the number of processes also requires adapting
the "signals", "Nps" and "rates" variables that are used when fitting with combine.

At the end of the file, you can find the possible actions. None of them can be skipped when running the 
code, and they must be run one after the other.
The details of each of them can be found in the file "ModuleRunner_datacards.py", which will be 
directly called by "steer_datacards.py".
Crucial files for running the code are

- steer_datacards.py
    -> Controls the running of the code

- ModuleRunner_datacards
    -> Calls different sectors of the code for the command asked by the steer.
    This file is the backbone of the code and should be investigated first in case of errors, or modifications.

- createCombineRootFiles
    -> Creates formatted rootfiles for the fits. Also do simple tasks such as removing empty bins.
    For each file configuration, three different files can be created
        1. No Smearing
        2. Adding Statistical fluctuations
        3. With Smearing
    By default, the real Data file will be added statistical error, to create a Fake Data.

    -> All the input files, created and formatted by "createCombineRootFiles.py", are stored at
"PostAnalyzer/datacards/rootfiles_for_datacards"

- plotter_andrea
    -> Plotter for the file, after having been fitted with combine

- collectShapesFromCombine
    -> Collects the plots and merge them to create the final result.

Producing the files relies on the folder structure in the code, which should not be modified, and should
be adapted if new processes or mass regions are added to the analysis. The outputs are stored as pdfs at 
"PostAnalyzer/datacards/Plots"

    -> The Final Plots are stored in a folder at /Plots/year/mass_region/results_PLOT_REGION_YEAR_DATATYPE_CHANNEL
    and contain the pdfs, as well as the fitting ratios.
    -> The Final Plots folders can not be overwritten. Therefore, they should be manually removed from the /Plots 
    folder, otherwise the code will not store them there.


For any questions or comments, feel free to reach out : benjamin.honore@epfl.ch