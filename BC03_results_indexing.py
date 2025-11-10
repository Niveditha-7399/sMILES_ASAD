
"""
This script is created by Niveditha Parthasarathy
to read the results obtained from the full-spectrum
fitting performed with Analyzer of integrated Spectra 
for Age, using the BC03 (Bruzual & Charlot 2003) models 

- results_file is the results file txt document.
- info_file is the bc03 model Index to age, 
metallicity information matching document.
- output_csv is the name of the results file
with the matched information added to it.
"""

#IMPORTING PACKAGES
import csv
import re

def match_results_to_info(results_file, info_file, output_csv):
    ###################################
    #READING MODEL FILE
    model_info = {}

    with open(info_file, 'r') as f:
        lines = f.readlines()

    #Skipping first line (like "150  [N_base]") 
    #second line will be the header, if present.
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = re.split(r'\s+', line.strip())
        filename = parts[0]

        #Extracting the numbers of mXX and ssp_YYY from filename
        match = re.search(r'_m(\d+).*_ssp_(\d{3})\.spec$', filename)
        if not match:
            continue

        m_val = match.group(1) #like: '22'
        ssp_val = match.group(2)    #like: '020'
        combined_key = m_val + ssp_val  #like '22020'
        
        model_info[combined_key] = parts


    ###################################
    #READING RESULTS FILE
    with open(results_file, 'r') as f:
        result_lines = f.readlines()

    #Parsing the header
    result_header = re.split(r'\s{2,}|\t+', result_lines[0].strip())

    #This tells code where to insert the info columns (after 'Minimum Age')
    insert_after_idx = result_header.index('Minimum Age') + 1

    #Use model info header from second line of info file
    model_info_header = ['spec-file', 'age[yr]', 'Z', 'code', 'Mstar', 'YAV?', 'a/Fe']

    #Final header
    final_header = result_header[:insert_after_idx] + model_info_header + result_header[insert_after_idx:]

    output_rows = [final_header]

    for line in result_lines[1:]:
        if not line.strip():
            continue
        parts = re.split(r'\s{2,}|\t+', line.strip())

        try:
            min_age = int(float(parts[1]))  #For example, 52078.0 becomess 52078
            min_age_str = str(min_age).zfill(5)  #making sure that it is 5 digits
            match_key = min_age_str  #Like '52078'
        except:
            match_key = None

        matched_info = model_info.get(match_key, ['N/A'] * len(model_info_header))

        #Inserting the matched info after Minimum Age column
        new_row = parts[:insert_after_idx] + matched_info + parts[insert_after_idx:]
        output_rows.append(new_row)


    ###############################
    #WRITING RESULTS
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print(f"Done! The results CSV with more BC03 model information is saved to: {output_csv}")


match_results_to_info(results_file='results_bc02_smiles_matched_model_asad_run.txt',info_file='Base_BC03_info.dat',output_csv='results_bc02_smiles_matched_model_asad_run.csv')

