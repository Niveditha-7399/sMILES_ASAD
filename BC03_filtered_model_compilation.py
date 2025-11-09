"""
This script is created by Niveditha Parthasarathy
to create a single model file from a folder full of 
BC03 (Bruzual & Charlot 2003) models but retaining only
the models mentioned in a text document 'base_info_file'.

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

def combine_spec_files_from_base_info(
    input_folder='bc03_models_resampled_step_1',
    base_info_file='Base_BC03_info_matched_smiles.dat',
    output_file='All_BC03_models_step1_txt_selected_range.txt'
):
    #Chooses just the text files from the model (input) folder
    #that are also in 'base_info_file'
    allowed_files = []
    with open(base_info_file, 'r') as f:

        for line in f:
            line = line.strip()
            #does not take header data
            if not line or line.startswith('#') or '[N_base]' in line:
                continue  
            parts = line.split()
            if len(parts) >= 1:
                spec_name = parts[0].strip()

                #Since only text documents are selected from the 
                #input folder, the name from the text document is
                #changed from .spec to .txt to find matches
                if spec_name.endswith('.spec'):
                    spec_name = spec_name.replace('.spec', '.txt')
                allowed_files.append(spec_name)

    print(f"Found {len(allowed_files)} model names in {base_info_file}")

    #Get the text files in the input folder
    spec_files = sorted(glob.glob(os.path.join(input_folder, "*.txt")))

    #Find matches iwth the text document
    spec_files = [f for f in spec_files if os.path.basename(f) in allowed_files]

    if not spec_files:
        print("No matching .txt files found that correspond to Base.BC03_info.txt")
        return

    print(f"Including {len(spec_files)} models from {input_folder}")

    #creating the model file
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
            if not line.strip().startswith('#') and line.strip():
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

    print(f" Combined model written to: {output_file}")


combine_spec_files_from_base_info()

