"""
This script is created by Niveditha Parthasarathy
to create a single model file from a folder full of 
BC03 (Bruzual & Charlot 2003) models

The BC03 model compilation was used for testing
with some outliers in the observations as well as
the sMILES models

It creates a single model file to be compatible
with Analyzer of integrated Spectra for Age

"""

#IMPORTING PACKAGES
import os
import glob
import re


def combine_spec_files_with_indices(input_folder='bc03_models_resampled_step_1', output_file='All_BC03_models_step1_txt.txt'):
    
    #Chooses just the text files from the model (input) folder
    spec_files = sorted(glob.glob(os.path.join(input_folder, "*.txt")))
    if not spec_files:
        print("No .txt files found in the folder.")
        return

    wavelengths = []
    all_fluxes = []
    indices = []

    for file_index, filepath in enumerate(spec_files):
        with open(filepath, 'r') as f:
            lines = f.readlines()

        #For example: bc2003_hr_m22_chab_ssp_020.spec
        #the index is stored as: m22 + ssp_020:- 22020
        filename = os.path.basename(filepath)
        match = re.search(r'_m(\d+).*_ssp_(\d+)\.txt$', filename)
        if not match:
            raise ValueError(f"Could not extract combined index from filename: {filename}")
       
        m_number = match.group(1) #Like '22'
        ssp_number = match.group(2) #Like '020'
        #The string '22020' is created
        combined_index = f"{m_number}{ssp_number}" 
        #And added to an index list
        indices.append(combined_index) 

        #ignore comments with #
        #find the first line without # for retrieving its data
        data_start = 0
        for i, line in enumerate(lines):
            if not line.strip().startswith('#'):
                data_start = i
                break

        current_wavelengths = []
        fluxes = []

        #consider only the lines without #
        #for each such line:
        #if its an empty string '' or has more info
        #than two column data, then skip the turn
        #otherwise: add the flux and wavelength 
        #to corresponding lists
        for line in lines[data_start:]:
            if line.strip() == '':
                continue
            parts = line.strip().split()
            if len(parts) != 2:
                continue
            wl, flux = float(parts[0]), float(parts[1])
            current_wavelengths.append(wl)
            fluxes.append(flux)

        #data from different model file
        #must have the same wavelength range
        if file_index == 0:
            wavelengths = current_wavelengths
        #otherwise show error here:
        else:
            if current_wavelengths != wavelengths:
                raise ValueError(f"Wavelength mismatch in file: {filepath}")

        all_fluxes.append(fluxes)

    #formatting
    combined_lines = []
    header = "# " + ", ".join(indices) + "\n"
    combined_lines.append(header)

    #for i-th each value of wavelength,
    #iterates over each model file data at j
    #and obtains the flux at i,
    #hence finding wavelength and the corresponding flux1, flux2 , ... 
    for i in range(len(wavelengths)):
        flux_row = [f"{all_fluxes[j][i]:.6E}" for j in range(len(all_fluxes))]
        line = f"{wavelengths[i]:.6E} " + " ".join(flux_row)
        combined_lines.append(line + "\n")

    #create the new model file
    with open(output_file, 'w') as f:
        f.writelines(combined_lines)

    print(f"Combined model written to: {output_file}")


combine_spec_files_with_indices()

